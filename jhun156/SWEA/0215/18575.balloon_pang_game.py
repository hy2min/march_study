# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    ans_result = []
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    def pang_game(y,x):

        sum = arr[y][x]
        directY = [0,0,1,-1]
        directX = [1,-1,0,0]
        for i in range(4):
            for j in range(1,N):
                dy = y + directY[i] * j
                dx = x + directX[i] * j
                if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1:
                    continue
                sum += arr[dy][dx]
        return sum

    for i in range(N):
        for j in range(N):
            ans_result.append(pang_game(i,j))
    Max = max(ans_result)
    Min = min(ans_result)
    ans = Max - Min
    print(f"#{tc} {ans}")
