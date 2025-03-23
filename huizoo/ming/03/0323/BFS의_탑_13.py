# 하이퍼 튜브
import sys
from collections import deque
input = sys.stdin.readline

# N : 역의 수, K : 하이퍼 튜브에 연결된 역의 수, M : 하이퍼 튜브의 수
N, K, M = map(int, input().split())
arr = [[] for _ in range(N+M+1)]
# 하이퍼 튜브는 N + 1 부터 시작
for i in range(N+1, N+M+1):
    arr2 = list(map(int, input().split()))
    for j in arr2:
        arr[j].append(i)
        arr[i].append(j)

def bfs():
    q = deque([1])
    # 하이퍼 튜브와 역 모두 방문체크 하면 좋음
    # 한번 이용한 하이퍼 튜브의 재사용은 최단거리에 필요 없기 때문
    visited = [0]*(N+M+1)
    visited[1] = 1
    while q:
        now = q.popleft()
        for hyper in arr[now]:
            if visited[hyper] == 0:
                visited[hyper] = 1
                for nxt in arr[hyper]:
                    if nxt == N:
                        return visited[now] + 1
                    if visited[nxt] == 0:
                        visited[nxt] = visited[now] + 1
                        q.append(nxt)

    return -1

if N == 1:
    print(1)
else:
    print(bfs())