# 어린이날 여행
import sys
from collections import deque
input = sys.stdin.readline

# N : 도시 개수, M : 도로 개수, K : 남은 기름통 칸 수, P : 출발 도시 번호
N, M, K, P = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

def bfs():
    q = deque([(P, K)])
    visited = [0]*(N+1)
    visited[P] = 1
    candidate = []
    while q:
        now, rest = q.popleft()
        for nxt in arr[now]:
            if visited[nxt] == 0:
                if rest == 1:
                    visited[nxt] = 1
                    candidate.append(nxt)
                elif rest > 1:
                    visited[nxt] = 1
                    q.append((nxt, rest-1))
    if len(candidate) != 0:
        return '\n'.join(map(str, sorted(candidate)))
    else:
        return -1

print(bfs())