# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    def kill_fly(y,x):
        Sum = 0
        for i in range(M):
            for j in range(M):
                Sum += arr[y+i][x+j]
        return Sum

    Max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = kill_fly(i,j)
            if Max < tmp:
                Max = tmp

    print(f"#{tc} {Max}")