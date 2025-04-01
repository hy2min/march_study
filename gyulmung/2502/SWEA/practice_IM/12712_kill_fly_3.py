import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def kill_cross(y, x, N, M):
    direct_X = [1, -1, 0, 0, -1, -1, 1, 1]
    direct_Y = [0, 0, 1, -1, 1, -1, 1, -1]
    Max = -1e8
    Sum = y + x
    for i in range(4):
        for j in range(1, M):
            dy = y + direct_Y[i]*j
            dx = x + direct_X[i]*j
            if dy < 0 or dx < 0 or dy >= N or dx >= N:
                continue
            else:
                Sum += arr[dy][dx]
                if Max < Sum:
                    Max = Sum
    Sum = y + x
    for i in range(4,8):
        for j in range(1, M):
            dy = y + direct_Y[i]*j
            dx = x + direct_X[i]*j
            if dy < 0 or dx < 0 or dy >= N or dx >= N:
                continue
            else:
                Sum += arr[dy][dx]
                if Max < Sum:
                    Max = Sum
    return Max

for test in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    Max_result = -1e8
    for i in range(n):
        for j in range(n):
            result = kill_cross(i, j, n, m)
            if Max_result < result:
                Max_result = result
    print(Max_result)