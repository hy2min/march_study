

T = int(input())
for idx in range(T):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]


    MaxSum = -21e8

    d_y = [-1,-1,-1,0,0,1,1,1]
    d_x = [-1,0,1,-1,1,-1,0,1]

    used = [[0]* m for _ in range(n)]
    MaxSum = -21e8

    def abc(y,x,level,Sum, used):
        global MaxSum
        if level == 4:
            if MaxSum < Sum:
                MaxSum = Sum
            return


        for i in range(8):
            dy = y + d_y[i]
            dx = x + d_x[i]
            if dy < 0 or dx < 0 or dy > n-1 or dx > m-1:
                continue
            if not used[dy][dx]:
                used[dy][dx] = 1
                abc(dy, dx, level+1, Sum + arr[dy][dx],used)
                used[dy][dx] = 0


    for i in range(n):
        for j in range(m):
            used[i][j] = 1
            abc(i,j,1, arr[i][j], used)
    print(MaxSum)


