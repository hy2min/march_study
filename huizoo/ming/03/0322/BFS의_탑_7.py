# 이사
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

R, K = map(int, input().split())

q = deque([(R, 0)])
visited = [0]*(N+1)
visited[R] = 1
cnt = 1
while q:
    now, cost = q.popleft()
    if cost == K: continue
    for nxt in arr[now]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            cnt += 1
            q.append((nxt, cost+1))

print(cnt)