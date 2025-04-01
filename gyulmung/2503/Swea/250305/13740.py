import sys
sys.stdin = open('input.txt', 'r')
# 3중 for문 이용
T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = []

    for i in range(N):
        for j in range(N):
            div_index = j+M

            if div_index > N:
                break

            slice_x = arr[i][j:div_index]
            slice_y = [arr[k][i] for k in range(j, div_index)]

            if slice_x == slice_x[::-1]:
                ans = slice_x
            if slice_y == slice_y[::-1]:
                ans = slice_y

    print(f'#{test} ', *ans, sep='')

# 진우형 소스코드

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    row_lst = [list(input()) for _ in range(N)]
    col_lst = list(map(list, zip(*row_lst)))

    answer = []
    for i in range(N):
        for j in range(N):
            slice_index = j + M

            if slice_index > N:
                break

            slice_row = row_lst[i][j:slice_index]
            slice_col = col_lst[i][j:slice_index]

            if slice_row == slice_row[::-1]:
                answer = slice_row
            if slice_col == slice_col[::-1]:
                answer = slice_col

    print(f'#{tc}', end=" ")
    for i in answer:
        print(i, end="")
    print()
