import sys
sys.stdin = open("input.txt", "r")


def check(y, x):
    global Max
    distance = [0]*d
    for y1, x1 in home:
        distance[abs(y1-y) + abs(x1-x) + 1] += 1

    can_service = 0
    for i in range(d):
        if distance[i]:
            can_service += distance[i]
            profit = can_service*M - (i**2 + (i-1)**2)
            if profit >= 0:
                Max = max(can_service, Max)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = tuple(tuple(map(int, input().split())) for _ in range(N))
    home = set()
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                home.add((i, j))

    d = 2*N
    Max = 0
    for i in range(N):
        for j in range(N):
            check(i, j)

    print(f'#{tc} {Max}')