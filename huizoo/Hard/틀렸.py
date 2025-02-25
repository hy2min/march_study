'''

틀렸으니까 나중에 꼭 다시 풀어보기
프로세서_연결하기

'''

import copy

def dfs(level, line):
    global arr, sum_line
    arr2 = copy.deepcopy(arr)
    if level == cnt:
        if sum_line > line:
            sum_line = line
            return
    for y, x in core:
        if arr[y][x] == 1 and [y, x] not in path:
            path.append([y, x])
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                temp_line = 0
                if arr[ny][nx] == 0:
                    if i == 0 :
                        flag = 0
                        for j in range(ny, -1, -1):
                            if arr[j][nx] != 0:
                                flag = 1
                        if flag:
                            continue
                        else:
                            for j in range(ny, -1, -1):
                                arr[j][nx] = 2
                                temp_line += 1
                    elif i == 1:
                        if sum(arr[ny][:nx]) == 0:
                            for j in range(nx):
                                arr[ny][j] = 2
                                temp_line += 1
                    elif i == 2:
                        flag = 0
                        for j in range(ny+1, N-1):
                            if arr[j][nx] != 0:
                                flag = 1
                        if flag:
                            continue
                        else:
                            for j in range(ny+1, N-1):
                                arr[j][nx] = 2
                                temp_line += 1
                    elif i == 3:
                        if sum(arr[ny][nx+1:]) == 0:
                            for j in range(nx+1, N):
                                arr[ny][j] = 2
                                temp_line += 1
                dfs(level+1, line+temp_line)
                arr = copy.deepcopy(arr2)
            path.pop()


t = int(input())
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    core = []
    path = []
    sum_line = 21e8

    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j] == 1:
                core.append([i, j])
                cnt += 1

    dfs(0, 0)

    print(f'#{tc} {sum_line}')