import sys
sys.stdin = open('input.txt', 'r')

t = int(input())


def row(y, x, m):
    cnt = 0
    for j in range(x + 1, m):
        if arr[y][j] == 1:
            cnt += 1
        else:
            break
    return cnt


def col(y, x, n):
    cnt = 0
    for i in range(y, n):
        if arr[i][x] == 1:
            cnt += 1
        else:
            break
    return cnt


for test in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_row_cnt = -21e8
    max_col_cnt = -21e8

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                res = row(i, j - 1, m)
                if res > max_row_cnt:
                    max_row_cnt = res

    for x in range(m):
        for y in range(n):
            if arr[y][x] == 1:
                res = col(y, x, n)
                if res > max_col_cnt:
                    max_col_cnt = res

    print(f'#{test} {max(max_col_cnt, max_row_cnt)}')