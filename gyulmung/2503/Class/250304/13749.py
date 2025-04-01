import sys
sys.stdin = open('input.txt', 'r')

def Find_x(y, x):
    cnt = 0
    for i in range(K+1):
        if x + i >= N or x-1 <0: continue
        if arr[y][x-1]==0 and arr[y][x+i] == 1:
            cnt += 1
    if cnt == K:
        return 1
    else:
        return 0

def Find_y(y, x):
    cnt = 0
    for i in range(K+1):
        if y + i >= N or y - 1 < 0: continue
        if arr[y-1][x]==0 and arr[y+i][x] == 1:
            cnt += 1
    if cnt == K:
        return 1
    else:
        return 0


T = int(input())

for test in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Y, X = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                X += Find_x(i,j)
                Y += Find_y(i,j)
    print(f'#{test} {X+Y}')