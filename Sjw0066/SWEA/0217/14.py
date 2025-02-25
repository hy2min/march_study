def miro(y,x):
    global flag

    direct_y = [0, 0, 1, -1]
    direct_x = [-1, 1, 0, 0]

    if lst[y][x] == 3:
        flag=1
        return

    for i in range(4):
        dy=direct_y[i]+y
        dx=direct_x[i]+x
        if dx<0 or dx>N-1 or dy<0 or dy>N-1:continue
        if lst[dy][dx] == 1 :continue
        if visited[dy][dx] == 1: continue

        visited[dy][dx] = 1
        miro(dy,dx)
        if flag:
            return


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    lst=[list(map(int,input())) for _ in range(N)]

    flag = 0
    visited = [[0] * N for _ in range(N)]
    st_y = 0
    st_x = 0

    for i in range(N):
        for j in range(N):
            if lst[i][j] == 2 :
                st_y=i
                st_x=j
    visited[st_y][st_x] = 1
    miro(st_y,st_x)
    print(f'#{tc} {flag}')

# def abc(y, x):
#     global flag
#     direct_y = [0, 0, -1, 1]
#     direct_x = [1, -1, 0, 0]
#
#     if y == ed[0] and x == ed[1]:
#         flag = 1
#         return
#     for i in range(4):
#         dy = y + direct_y[i]
#         dx = x + direct_x[i]
#         if dx < 0 or dy < 0 or dx >= N or dy >= N: continue
#         if arr[dy][dx] == '1': continue
#         if visited[dy][dx] == 1: continue
#         visited[dy][dx] = 1
#         abc(dy, dx)
#         if flag:
#             return
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(str, input())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     flag = 0
#     st = []
#     ed = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == '2':
#                 st = [i, j]
#             if arr[i][j] == '3':
#                 ed = [i, j]
#     visited[st[0]][st[1]] = 1
#     abc(st[0], st[1])
#     print(f'#{tc} {flag}')
