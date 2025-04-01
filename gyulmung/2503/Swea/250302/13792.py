import sys
sys.stdin = open('input.txt','r')

def Tile(N):
    if N % 10 != 0:
        return 0
    n = N // 10
    tile = [0]*(n+1)
    tile[1] = 1
    tile[2] = 3
    if n >= 3:
        for i in range(3, n+1):
            tile[i] = tile[i-1] + 2*tile[i-2]
    return tile[n]

T = int(input())
for test in range(1, T+1):
    N = int(input())
    result = Tile(N)
    print(f'#{test} {result}')