def abc(arr):
    global ans
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                ans = arr[i][j:j+M]

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    arr2 = list(zip(*arr))
    ans = []
    abc(arr)
    abc(arr2)
    print(f'#{tc} {"".join(ans)}')