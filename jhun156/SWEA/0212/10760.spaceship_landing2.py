# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    def check(y,x):
        default = arr[y][x]
        cnt = 0
        directY = [0,0,1,-1,1,1,-1,-1]
        directX = [1,-1,0,0,1,-1,1,-1]
        for i in range(8):
            dy = y + directY[i]
            dx = x + directX[i]
            if dy < 0 or dy > N-1 or dx < 0 or dx > M -1:
                continue
            if arr[dy][dx] < default:
                cnt += 1
        if cnt >= 4:
            return 1
        else:
            return 0

    ans = 0
    for i in range(N):
        for j in range(M):
            tmp = check(i,j)
            ans += tmp
    print(f"#{tc} {ans}")