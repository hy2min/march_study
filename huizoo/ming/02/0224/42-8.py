from collections import deque
n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
visited = [[0]*n for _ in range(n)]
def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0<=ny<n and 0<=nx<n:
                if arr[ny][nx]: continue
                if visited[ny][nx]: continue
                if ny == n-1 and nx == n-1:
                    return '가능'
                visited[ny][nx] = 1
                q.append((ny, nx))
    return '불가능'

print(bfs())