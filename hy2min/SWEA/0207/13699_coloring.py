T = int(input())
for idx in range(T):
    arr = [[0] * 10 for _ in range(10)]

    N = int(input())
    for _ in range(N):

        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if arr[i][j] == color:
                    continue
                elif arr[i][j] != 0:
                    arr[i][j] = -1
                else:
                    arr[i][j] = color

    cnt = 0
    for i in arr:
        for j in i:
            if j == -1:
                cnt += 1
    print(f'#{idx+1} {cnt}')
