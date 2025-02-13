import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def find_ruins_col(y, x, M):
    count = 0
    for i in range(M):
        if x + i > M - 1:
            break
        elif arr[y][x + i] == 0:
            break
        elif arr[y][x + i] == 1:
            count += 1
    return count

def find_ruins_wid(y, x, N):
    count = 0
    for i in range(N):
        if y + i > N - 1:
            break
        elif arr[y + i][x] == 0:
            break
        elif arr[y + i][x] == 1:
            count += 1
    return count


for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Max = 0
    for j in range(N):
        for k in range(M):
            if arr[j][k] == 1:
                count_col = find_ruins_col(j, k, M)
                if Max < count_col:
                    Max = count_col
                count_wid = find_ruins_wid(j, k, N)
                if Max < count_wid:
                    Max = count_wid

    print(f'#{i} {Max}')