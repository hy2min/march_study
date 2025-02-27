import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def find_LR(y, x, arr, N):

    direct_Y = [0, 0]
    direct_X = [1, -1]
    count_T = 0
    count = 0
    for i in range(2):
        for puls in range(1, 3):
            dy = (direct_Y[i] * puls) + y
            dx = (direct_X[i] * puls) + x
            if dy < 0 or dx < 0 or dy >= N or dx >= N:
                break
            if arr[dy][dx] == 'o':
                count += 1
            elif arr[dy][dx] != 'o':
                count = 0
                break
    if count >= 4:
        count_T = 1
    return count_T


def find_UD(y, x, arr, N):
    direct_Y = [1, -1]
    direct_X = [0, 0]
    count_T = 0
    count = 0
    for i in range(2):
        for puls in range(1, 3):
            dy = (direct_Y[i] * puls) + y
            dx = (direct_X[i] * puls) + x
            if dy < 0 or dx < 0 or dy >= N or dx >= N:
                break
            if arr[dy][dx] == 'o':
                count += 1
            elif arr[dy][dx] != 'o':
                count = 0
                break
    if count >= 4:
        count_T = 1
    return count_T


def find_UDC(y, x, arr, N):
    direct_Y = [1, -1]
    direct_X = [1, -1]
    count_T = 0
    count = 0
    for i in range(2):
        for puls in range(1, 3):
            dy = (direct_Y[i] * puls) + y
            dx = (direct_X[i] * puls) + x
            if dy < 0 or dx < 0 or dy >= N or dx >= N:
                break
            if arr[dy][dx] == 'o':
                count += 1
            elif arr[dy][dx] != 'o':
                count = 0
                break
    if count >= 4:
        count_T = 1
    return count_T


def find_LRC(y, x, arr, N):
    direct_Y = [-1, 1]
    direct_X = [1, -1]
    count_T =0
    count = 0
    for i in range(2):
        for puls in range(1, 3):
            dy = (direct_Y[i] * puls) + y
            dx = (direct_X[i] * puls) + x
            if dy < 0 or dx < 0 or dy >= N or dx >= N:
                break
            if arr[dy][dx] == 'o':
                count += 1
            elif arr[dy][dx] != 'o':
                count = 0
                break
    if count >= 4:
        count_T = 1
    return count_T

for test in range(4, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    count_T = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                count_T += find_LR(i, j, arr, N)
                count_T += find_UD(i, j, arr, N)
                count_T += find_LRC(i, j, arr, N)
                count_T += find_UDC(i, j, arr, N)
            if count_T >= 1:
                break

    if count_T >= 1:
        print(f'#{test} YES')
    else:
        print(f'#{test} NO')
