def check(y,x):
    d_y = [-1,0,1,1] # 1시 3시 5시 6시 방향
    d_x = [1,1,1,0]
    for i in range(4):
        cnt = 0
        for j in range(5):  # 5개 연속 체크
            dy = y + d_y[i] * j
            dx = x + d_x[i] * j
            if dy < 0 or dx < 0 or dy >= N or dx >= N: continue
            if arr[dy][dx] == 'o':
                cnt += 1
        if cnt == 5:
            return 1
    return 0
T = int(input())
for idx in range(T):
    ans = "NO"
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            ret = check(i,j)
            if ret == 1:
                ans = "YES"
                break
        if ans == "YES":
            break
    print(f'#{idx+1} {ans}')

