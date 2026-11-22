"""Sliding-window rate limits kept in memory, plus the real client IP behind Caddy."""
import threading
import time
from collections import defaultdict, deque

from flask import request

_hits = defaultdict(deque)
_lock = threading.Lock()


def client_ip():
    # Caddy overwrites X-Forwarded-For with the real client (the app port is not public), so the first entry is trusted.
    return (request.headers.get('X-Forwarded-For') or request.remote_addr or '').split(',')[0].strip()


def too_many(key, limit, window, hit=True):
    """Record one hit for key (unless hit=False: only look); True when more than limit hits happened in the last window seconds.
    shortcut: per gunicorn worker (2 workers, so up to 2x the limit), move to Redis if the app scales out."""
    now = time.monotonic()
    with _lock:
        q = _hits[key]
        while q and q[0] <= now - window:
            q.popleft()
        if len(q) >= limit:
            return True
        if hit:
            q.append(now)
        if len(_hits) > 50_000:  # bound memory against key floods
            _hits.clear()
        return False
