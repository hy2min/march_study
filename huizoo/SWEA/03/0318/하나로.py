from math import sqrt
import sys
sys.stdin = open("input.txt", "r")

def findboss(x):
    if parent[x] != x:
        parent[x] = findboss(parent[x])
    return parent[x]

def union(a, b, idx):
    global cnt, total
    bossA, bossB = findboss(a), findboss(b)
    if bossA == bossB:
        return
    if rank[bossA] < rank[bossB]:
        parent[bossA] = bossB
    else:
        parent[bossB] = bossA
        if rank[bossB] == rank[bossA]:
            rank[bossA] += 1
    cnt += 1
    total += E*arr2[i][2]**2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    E = float(input())
    arr2 = []
    for i in range(N-1):
        for j in range(i+1, N):
            gap = sqrt((arr[0][i] - arr[0][j]) ** 2 + (arr[1][i] - arr[1][j]) ** 2)
            arr2.append((i, j, gap))
    arr2.sort(key=lambda x: x[2])
    parent = [i for i in range(N)]
    rank = [1]*N
    cnt = 0
    total = 0
    M = len(arr2)
    for i in range(M):
        if cnt == N-1:
            break
        union(arr2[i][0], arr2[i][1], i)
    print(f'#{tc} {round(total)}')