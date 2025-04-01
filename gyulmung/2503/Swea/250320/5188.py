import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    lst = [[0]*n for _ in range(n)]
    lst[0][0] = arr[0][0]
    for i in range(1, n):
        lst[0][i] = arr[0][i]+lst[0][i-1]
        lst[i][0] = arr[i][0]+lst[i-1][0]
    for i in range(1, n):
        for j in range(1, n):
            lst[i][j] = min(lst[i-1][j]+arr[i][j], lst[i][j-1]+arr[i][j])
    print(f'#{test} {lst[n - 1][n - 1]}')
