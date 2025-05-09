# 네트워크 바이러스
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0
q = deque([1])
visited = [0]*(N+1)
visited[1] = 1
while q:
    now = q.popleft()
    for nxt in arr[now]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            q.append(nxt)
            cnt += 1

print(cnt)