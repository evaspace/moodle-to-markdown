"""Product statistics for the admin dashboard (/admin/stats). Aggregated, no usernames."""
from collections import Counter, defaultdict
from datetime import timedelta

MAX_SECS = 1800     # one attempt counts at most 30 min (tab left open)
MIN_ATTEMPTS = 5    # an exercise needs this many attempts to be ranked as hard


EVENTS = ('niveau_up', 'niveau_down', 'passer', 'aide', 'copie_ia')
OWNER_COLOR = '#2563C9'  # the site owner's share in every admin chart
DAYS = ['lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim']


def week_heat(datetimes):
    """7 rows (Monday first) x 24 hour cells; colour goes from white (nothing) to green (the busiest slot)."""
    grid = [[0] * 24 for _ in DAYS]
    for t in datetimes:
        grid[t.weekday()][t.hour] += 1
    top = max(max(r) for r in grid) or 1
    return [{'day': DAYS[i], 'total': sum(r), 'cells': [
        {'h': h, 'n': n, 'color': f'hsl(130, 62%, {round(97 - 59 * (n / top) ** 0.6)}%)' if n else '#fff'}
        for h, n in enumerate(r)]} for i, r in enumerate(grid)]


def _pct(a, b):
    return round(100 * a / b) if b else 0


def _series(counter, days):
    top = max([counter.get(d, 0) for d in days] + [1])
    return [{'label': f'{d.day}/{d.month}', 'n': counter.get(d, 0), 'h': round(100 * counter.get(d, 0) / top)} for d in days]


def _stack(a, b):
    """Stack two same-day series: others (green, h) under the owner (blue, hm), scaled on the combined top."""
    top = max([x['n'] + y['n'] for x, y in zip(a, b)] + [1])
    return [{**x, 'me': y['n'], 'h': round(100 * x['n'] / top), 'hm': round(100 * y['n'] / top)} for x, y in zip(a, b)]


def compute(accounts, logs, progress, paths, today, events=(), owner_ids=()):
    """Stats of every account except owner_ids, with the owner's own stats under 'me' (shown in blue),
    and charts stacked: others then the owner on top."""
    own = set(owner_ids)
    split = lambda rows, k: ([r for r in rows if r.get(k) not in own], [r for r in rows if r.get(k) in own])
    (a0, a1), (l0, l1), (p0, p1), (e0, e1) = (split(accounts, 'id'), split(logs, 'account_id'),
                                              split(progress, 'account_id'), split(events, 'account_id'))
    s, m = _compute(a0, l0, p0, paths, today, e0), _compute(a1, l1, p1, paths, today, e1)
    for k in ('signup_chart', 'exo_chart'):
        s[k] = _stack(s[k], m[k])
    for row, mrow in zip(s['heat'], m['heat']):
        row['me'] = mrow['total']
        for c, mc in zip(row['cells'], mrow['cells']):
            if mc['n']:  # owner share as a solid blue fill from the bottom of the cell
                cut = round(100 * mc['n'] / (mc['n'] + c['n']))
                c['color'] = f"linear-gradient(to top, {OWNER_COLOR} {cut}%, {c['color']} {cut}%)"
            c['me'] = mc['n']
    mf = {f['id']: f for f in m['funnel']}
    for f in s['funnel']:
        f['me'] = g = mf[f['id']]
        total = f['started'] + g['started']
        f['bars'] = [{**b, 'me': gb['n'], 'h': _pct(b['n'], total), 'hm': _pct(gb['n'], total)}
                     for b, gb in zip(f['bars'], g['bars'])]
    s['funnel'].sort(key=lambda f: -(f['started'] + f['me']['started']))
    for h in s['hard']:
        h['me'] = m['_exo'].get(h['key'], [0])[0]
    s.pop('_exo'), m.pop('_exo')
    s['me'] = m
    return s


def _compute(accounts, logs, progress, paths, today, events=()):
    """accounts: [{id, created(date), email}], logs: [{account_id, subject, level, exo_id, ok, secs, peek, timeout, at(datetime)}],
    progress: [{account_id, subject, level, best}], paths: {subject_id: {'titre', 'levels': n}},
    events: event_log rows [{kind, at(datetime)}] (skips, helps, AI copies, level changes)."""
    from levels import week_history
    created = {a['id']: a['created'] for a in accounts}
    by_user = defaultdict(list)
    for r in logs:
        by_user[r['account_id']].append(r)
    active_days = {u: {r['at'].date() for r in rs} for u, rs in by_user.items()}

    def active_between(start, end):
        return sum(1 for ds in active_days.values() if any(start <= d <= end for d in ds))

    n_acc = len(accounts)
    done = len(logs)
    ok = sum(r['ok'] for r in logs)
    secs = sum(min(r['secs'] or 0, MAX_SECS) for r in logs)
    engaged = sum(1 for rs in by_user.values() if len(rs) >= 20)
    mau, wau, dau = (active_between(today - timedelta(days=n), today) for n in (29, 6, 0))

    # retention: signed up at least N days ago and active on a later day (D1 = the day after, D7 = within days 1..7)
    def retention(n):
        cohort = [u for u, c in created.items() if (today - c).days >= n]
        back = sum(1 for u in cohort if any(1 <= (d - created[u]).days <= n for d in active_days.get(u, ())))
        return {'cohort': len(cohort), 'back': back, 'pct': _pct(back, len(cohort))}

    last30 = [today - timedelta(days=29 - i) for i in range(30)]
    signups = Counter(c for c in created.values())
    per_day = Counter(r['at'].date() for r in logs)
    weekly = Counter()  # exercises per ISO week, last 8 weeks
    for r in logs:
        d = r['at'].date()
        if (today - d).days < 56:
            weekly[(today - d).days // 7] += 1

    # per path funnel: users who started / validated level k
    best = defaultdict(dict)
    stuck = defaultdict(Counter)
    for p in progress:
        best[p['subject']][p['account_id']] = p['best']
        stuck[p['subject']][p['level']] += 1
    starters = defaultdict(set)
    for r in logs:
        starters[r['subject']].add(r['account_id'])
    funnel = []
    for sid, meta in paths.items():
        n_lv, st = meta['levels'], starters.get(sid, set())
        reached = [sum(1 for u in st if best[sid].get(u, 0) >= k) for k in range(1, n_lv + 1)]
        sub = [r for r in logs if r['subject'] == sid]
        funnel.append({'id': sid, 'titre': meta['titre'], 'started': len(st), 'finished': reached[-1] if reached else 0,
                       'exos': len(sub), 'rate': _pct(sum(r['ok'] for r in sub), len(sub)),
                       'bars': [{'k': k + 1, 'n': v, 'h': _pct(v, len(st)) if st else 0} for k, v in enumerate(reached)],
                       'stuck': stuck[sid].most_common(1)[0] if stuck[sid] else None})
    funnel.sort(key=lambda f: -f['started'])

    per_exo = defaultdict(lambda: [0, 0, 0, 0])  # attempts, fails, secs, timeouts
    for r in logs:
        v = per_exo[(r['subject'], r['level'], r['exo_id'])]
        v[0] += 1
        v[1] += 1 - r['ok']
        v[2] += min(r['secs'] or 0, MAX_SECS)
        v[3] += r.get('timeout', 0)
    hard = sorted(((k, v) for k, v in per_exo.items() if v[0] >= MIN_ATTEMPTS), key=lambda kv: (-kv[1][1] / kv[1][0], -kv[1][0]))[:10]
    ev_all, ev_7d = Counter(), Counter()
    for e in events:
        k = 'aide' if e['kind'].startswith('aide_') else {'niveau_finished': 'niveau_up'}.get(e['kind'], e['kind'])
        ev_all[k] += 1
        ev_7d[k] += (today - e['at'].date()).days < 7
    return {
        'events': {k: {'all': ev_all[k], 'week': ev_7d[k]} for k in EVENTS},
        'history': week_history(logs, events, today),
        'accounts': n_acc, 'with_email': _pct(sum(1 for a in accounts if a.get('email')), n_acc),
        'activated': len(by_user), 'activation': _pct(len(by_user), n_acc), 'engaged': engaged,
        'exercises': done, 'success': _pct(ok, done), 'hours_spent': round(secs / 3600, 1),
        'timeout_rate': _pct(sum(r.get('timeout', 0) for r in logs), done),
        'peek_rate': _pct(sum(1 for r in logs if r.get('peek')), done),
        'dau': dau, 'wau': wau, 'mau': mau, 'stickiness': _pct(dau, mau),
        'new_7d': sum(v for d, v in signups.items() if (today - d).days < 7),
        'new_30d': sum(v for d, v in signups.items() if (today - d).days < 30),
        'per_active_user': round(done / len(by_user), 1) if by_user else 0,
        'minutes_per_active_day': round(secs / 60 / max(1, sum(len(d) for d in active_days.values()))),
        'retention': {'d1': retention(1), 'd7': retention(7), 'd30': retention(30)},
        'signup_chart': _series(signups, last30), 'exo_chart': _series(per_day, last30),
        'heat': week_heat([r['at'] for r in logs]),
        'weekly': [weekly.get(i, 0) for i in range(7, -1, -1)],
        'funnel': funnel,
        '_exo': {'|'.join(map(str, k)): v for k, v in per_exo.items()},
        'hard': [{'key': '|'.join(map(str, k)), 'subject': paths.get(k[0], {}).get('titre', k[0]), 'level': k[1], 'exo': k[2], 'attempts': v[0],
                  'fail': _pct(v[1], v[0]), 'avg_secs': round(v[2] / v[0])} for k, v in hard],
    }
