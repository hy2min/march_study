import sys
input = sys.stdin.readline


def findboss(x):
    if par[x] != x:
        par[x] = findboss(par[x])
    return par[x]

def union(u, v):
    global cnt
    bossU, bossV = findboss(u), findboss(v)
    if bossU == bossV:
        return
    if rank[bossU] > rank[bossV]:
        par[bossV] = par[bossU]
    else:
        par[bossU] = par[bossV]
        if rank[bossU] == rank[bossV]:
            rank[bossV] += 1

    cnt += 1


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    par = [i for i in range(N+1)]
    rank = [1]*(N+1)

    cnt = 0
    for i in range(M):
        if cnt == N-1:
            break
        union(arr[i][0], arr[i][1])

    print(cnt)