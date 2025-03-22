# 인접행렬 BFS
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    arr2 = list(map(int, input().split()))
    for j in range(N):
        if arr2[j] == 1:
            arr[i].append(j)

q = deque([0])
visited = [0]*N
visited[0] = 1
while q:
    now = q.popleft()
    print(now, end=' ')
    for nxt in arr[now]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            q.append(nxt)