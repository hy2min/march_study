import sys
sys.stdin = open('input.txt', 'r')

def Pop(y, x, N):
    direct_Y = [0, 0, 1, -1]
    direct_X = [1, -1, 0, 0]
    cnt = 0
    for i in range(4):
        for j in range(1, N+1):
            dy = direct_Y[i]*j + y
            dx = direct_X[i]*j + x

            if dy < 0 or dx < 0 or dy >= N or dx >= N:
                continue

            cnt += arr[dy][dx]
    return cnt + arr[y][x]


T = int(input())

for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    result_lst = []
    for i in range(N):
        for j in range(N):
            cnt = Pop(i, j, N)
            result_lst.append(cnt)
    print(f'#{test} {max(result_lst) - min(result_lst)}')
