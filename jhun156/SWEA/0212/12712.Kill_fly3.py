# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    def Killfly(y,x):
        sum1,sum2 = arr[y][x],arr[y][x]
        directX = [0,0,1,-1]
        directY = [1,-1,0,0]
        crossX = [1,1,-1,-1]
        crossY = [1,-1,1,-1]
        for i in range(4):
            for j in range(1,M):
                dy = y + directY[i] * j
                dx = x + directX[i] * j
                if dy < 0 or dy > N-1 or dx < 0 or dx > N-1:
                    continue
                sum1 += arr[dy][dx]
        for i in range(4):
            for j in range(1,M):
                dy = y + crossY[i] * j
                dx = x + crossX[i] * j
                if dy < 0 or dy > N-1 or dx < 0 or dx > N-1:
                    continue
                sum2 += arr[dy][dx]
        return max(sum1,sum2)

    ans = 0
    for i in range(N):
        for j in range(N):
            tmp = Killfly(i,j)
            if ans < tmp:
                ans = tmp

    print(f"#{tc} {ans}")