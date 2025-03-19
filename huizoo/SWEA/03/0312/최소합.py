t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0: continue
            if i == 0:
                arr[i][j] += arr[i][j-1]
            elif j == 0:
                arr[i][j] += arr[i-1][j]
            else:
                arr[i][j] += min(arr[i-1][j], arr[i][j-1])
    print(f'#{tc} {arr[n-1][n-1]}')