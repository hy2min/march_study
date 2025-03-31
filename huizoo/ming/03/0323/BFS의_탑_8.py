# 출근
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
temp = tuple(tuple(map(int, input().split())) for _ in range(M))
T = int(input())
for a, b in temp:
    if a != T and b != T:
        arr[a].append(b)
        arr[b].append(a)

def bfs():
    q = deque([1])
    visited = [-1]*(N+1)
    visited[1] = 0
    while q:
        now = q.popleft()
        for nxt in arr[now]:
            if nxt == N:
                return visited[now] + 1
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + 1
                q.append(nxt)
    return -1

print(bfs())