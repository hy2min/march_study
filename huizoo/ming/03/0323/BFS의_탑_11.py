# 순간 이동
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([(N, 0)])
    visited = set([N])
    while q:
        now, cnt = q.popleft()
        for nxt in (now+1, now-1, now*2):
            if nxt == M:
                return cnt + 1
            if nxt < 0 or nxt > 10e4:
                continue
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, cnt + 1))

    return

N, M = map(int, input().split())

if N == M:
    print(0)
else:
    print(bfs())