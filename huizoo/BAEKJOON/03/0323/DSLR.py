import sys
from collections import deque
input = sys.stdin.readline

def d(x):
    return (2*x) % 10000, 'D'

def s(x):
    return 9999 if x == 0 else x-1, 'S'

def l(x):
    num = str(x)
    num = (4-len(num))*'0' + num
    return int(num[1:] + num[0]), 'L'

def r(x):
    num = str(x)
    num = (4 - len(num)) * '0' + num
    return int(num[-1] + num[:-1]), 'R'

def lock(a, b):
    q = deque([(a, '')])
    checked = set([a])
    while q:
        now, record = q.popleft()
        for nxt, way in (d(now), s(now), l(now), r(now)):
            if nxt == b:
                return record + way
            if nxt not in checked:
                checked.add(nxt)
                q.append((nxt, record+way))


N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    print(lock(A, B))