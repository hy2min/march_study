def check(y,x):
    cnt = 0
    d_y = [-1,-1,-1,0,0,1,1,1]
    d_x = [-1,0,1,-1,1,-1,0,1]
    for i in range(8):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if 0 <= dy < N and 0 <= dx < M:
            if arr[dy][dx] < arr[y][x]:
                cnt += 1
    return cnt

T = int(input())

for idx in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    space = 0
    for i in range(N):
        for j in range(M):
            if check(i,j) >= 4:
                space += 1

    print(f'#{idx+1} {space}')

