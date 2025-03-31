def check(y,x):
    d_y = [-1,-1,0,1]
    d_x = [0,1,1,1]
    for i in range(4):
        cnt = 0
        for j in range(5):
            dy = y + d_y[i] * j
            dx = x + d_x[i] * j
            if dy < 0 or dx < 0 or dy >= n or dx >= n:
                continue
            if arr[dy][dx] == 'o':
                cnt += 1
        if cnt == 5:
            return 1
    return 0


t = int(input())
for tc in range(1,t+1):
    ans = 'NO'
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if check(i,j):
                ans = 'YES'
                break
        if ans == 'YES':
            break
    print(f'#{tc} {ans}')
