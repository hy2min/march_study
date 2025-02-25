import sys
sys.setrecursionlimit(10**6)
R, C = map(int, sys.stdin.readline().split())
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(R)]

best_path = ''
if R % 2 == 1:
    best_path += 'R'*(C-1)
    for _ in range(R//2):
        best_path += 'D'+'L'*(C-1)+'D'+'R'*(C-1)
else:
    if C % 2 == 1:
        best_path += 'D'*(R-1)
        for _ in range(C//2):
            best_path += 'D'+'L'*(C-1)+'D'+'R'*(C-1)
    else:
        for i in range(R):
            for j in range(C):
                pass
#         for _ in range(R//2-1):
#             best_path += 'R'*(C-1)+'D'+'L'*(C-1)+'D'
#         for i in range((C-1)//2):
#             if i % 2 == 0:
#                 best_path += 'DR'
#             else:
#                 best_path += 'UR'
#         if arr[R-1][C-2] < arr[R-2][C-1]:
#             best_path += 'RD'
#         else:
#             best_path += 'DR'
#
# print(best_path)







#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# dd = 'UDLR'
# Max = 0
# visited = set()
# best_path = ''
# def dfs(y, x, Sum, path):
#     global Max, best_path
#     if y == R-1 and x == C-1:
#         if Max < Sum:
#             best_path = path
#             Max = Sum
#         return
#     for i in range(4):
#         ny, nx = y+dy[i], x+dx[i]
#         if ny<0 or nx<0 or ny>=R or nx>=C:continue
#         if (ny, nx) in visited:continue
#         visited.add((ny,nx))
#         dfs(ny, nx, Sum+arr[ny][nx], path+dd[i])
#         visited.remove((ny,nx))
#
# visited.add((0,0))
# dfs(0, 0, arr[0][0], '')
# print(best_path)
#
#
#
