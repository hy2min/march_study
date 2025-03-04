# import sys
#
# def dfs(y, x, Sum):
#     global Max
#     Max = max(Max, Sum)
#     for dy, dx in direct:
#         ny, nx = y+dy, x+dx
#         if ny<0 or nx<0 or ny>=N or nx>=M: continue
#         if arr[ny][nx] in path: continue
#         path.add(arr[ny][nx])
#         dfs(ny, nx, Sum+1)
#         path.remove(arr[ny][nx])
#
#
# N, M = map(int, sys.stdin.readline().split())
# arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# path = set()
# direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]
# Max = 0
# path.add(arr[0][0])
# dfs(0, 0, 1)
#
# print(Max)
#

from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j, arr[i][j]))
    visited = set()
    visited.add((i, j, arr[i][j]))

    Max = 1
    while q:
        y, x, path = q.popleft()
        Max = max(Max, len(path))

        for dy, dx in direct:
            ny, nx = y + dy, x + dx
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            if arr[ny][nx] in path:
                continue

            new_path = path + arr[ny][nx]
            if (ny, nx, new_path) not in visited:
                visited.add((ny, nx, new_path))
                q.append((ny, nx, new_path))

    return Max


N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]
direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]

print(bfs(0, 0))