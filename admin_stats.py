"""Product statistics for the admin dashboard (/admin/stats). Aggregated, no usernames."""
from collections import Counter, defaultdict
from datetime import timedelta

MAX_SECS = 1800     # one attempt counts at most 30 min (tab left open)
MIN_ATTEMPTS = 5    # an exercise needs this many attempts to be ranked as hard


def _pct(a, b):
    return round(100 * a / b) if b else 0


def _series(counter, days):
    top = max([counter.get(d, 0) for d in days] + [1])
    return [{'label': f'{d.day}/{d.month}', 'n': counter.get(d, 0), 'h': round(100 * counter.get(d, 0) / top)} for d in days]


def compute(accounts, logs, progress, paths, today):
    """accounts: [{id, created(date), email}], logs: [{account_id, subject, level, exo_id, ok, secs, peek, timeout, at(datetime)}],
    progress: [{account_id, subject, level, best}], paths: {subject_id: {'titre', 'levels': n}}."""
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
    hours, weekdays = Counter(r['at'].hour for r in logs), Counter(r['at'].weekday() for r in logs)
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
    return {
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
        'hours': [{'label': h, 'n': hours.get(h, 0), 'h': _pct(hours.get(h, 0), max(hours.values(), default=1))} for h in range(24)],
        'weekdays': [{'label': n, 'n': weekdays.get(i, 0), 'h': _pct(weekdays.get(i, 0), max(weekdays.values(), default=1))}
                     for i, n in enumerate(['lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim'])],
        'weekly': [weekly.get(i, 0) for i in range(7, -1, -1)],
        'funnel': funnel,
        'hard': [{'subject': paths.get(k[0], {}).get('titre', k[0]), 'level': k[1], 'exo': k[2], 'attempts': v[0],
                  'fail': _pct(v[1], v[0]), 'avg_secs': round(v[2] / v[0])} for k, v in hard],
    }
