# 뷰 포인트
import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

start = 1
q = deque([(1, 0)])
cnt = 0
while q:
    now, now_cost = q.popleft()
    for nxt, nxt_cost in arr[now]:
        if now_cost + nxt_cost <= K:
            q.append((nxt, now_cost + nxt_cost))
            cnt += 1

print(cnt)