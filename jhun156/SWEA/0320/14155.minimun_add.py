# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    for i in range(1,N):
        arr[0][i] += arr[0][i-1]
        arr[i][0] += arr[i-1][0]

    for i in range(1,N):
        for j in range(1,N):
            arr[i][j] = min(arr[i-1][j],arr[i][j-1]) + arr[i][j]
    print(f"#{tc} {arr[N-1][N-1]}")
