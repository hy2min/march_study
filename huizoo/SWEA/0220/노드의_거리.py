from collections import deque
def bfs(start):
    visited = [0]*(V+1)
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        for p in arr[now]:
            if not visited[p]:
                q.append(p)
                visited[p] = visited[now] + 1
    print(f'#{tc} {max(0, visited[G] - visited[S])}')


t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        arr[v1].append(v2)
        arr[v2].append(v1)
    S, G = map(int, input().split())
    bfs(S)
