# 인접행렬 BFS
import sys
from collections import deque
input = sys.stdin.readline

# N : 던전 개수, M : 경로의 개수, K : 골드
N, M, K = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

q = deque([(0, 0)])
dungeon = []
while q:
    now, cost = q.popleft()
    for nxt, nxt_cost in arr[now]:
        if cost+nxt_cost <= K:
            dungeon.append(nxt)
            q.append((nxt, cost+nxt_cost))

print(' '.join(map(str, sorted(dungeon))))