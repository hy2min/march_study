import sys
sys.stdin = open('input.txt', 'r')

test = int(input())

def Find_row(y, x, M):
    count_row = 0
    non = 0
    for i in range(M+1):
        if x > 0 and ai[y][x - 1] == 1:
            break
        elif x + i > M + 1:
            break
        elif ai[y][x+i] == 1:
            count_row += 1

    if count_row == M:
        return count_row // M
    else:
        return non

def Find_col(y, x, M):
    count_col = 0
    non = 0
    for i in range(M + 1):
        if y > 0 and ai[y - 1][x] == 1:
            break
        elif y + i > M + 1:
            break
        elif ai[y+i][x] == 1:
            count_col += 1

    if count_col == M:
        return count_col // M
    else:
        return non


for time in range(1, test + 1):
    N, M = map(int, input().split())
    ai = [list(map(int, input().split())) for _ in range(N)]
    count1 = 0
    count2 = 0

    for j in range(N):
        for k in range(0, N - M + 1):
            if ai[j][k] == 1:
                count1 += Find_row(j, k, M)
                count2 += Find_col(k, j, M)
    print(count1 + count2)