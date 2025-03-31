# 더블 리모콘
import sys
from collections import deque
input = sys.stdin.readline

def plus(x):
    return x + 1

def minus(x):
    return x - 1

def mul(x):
    return 2 * x

def dev(x):
    return x // 2

def bfs(a, b):
    q = deque([(a, 0)])
    visited = set([a])
    while q:
        now, cnt = q.popleft()
        if now == b:
            return cnt

        for nxt in (plus(now), minus(now), mul(now), dev(now)):
            if 0 <= nxt <= 100000 and nxt not in visited:
                visited.add(nxt)
                q.append((nxt, cnt + 1))

S = int(input())
D = int(input())
print(bfs(S, D))
