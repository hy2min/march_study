def findboss(x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x

def union(a, b):
    bossA, bossB = findboss(a), findboss(b)
    if bossA == bossB:
        return 1
    if rank[bossA] < rank[bossB]:
        par[bossA] = bossB
    else:
        par[bossB] = bossA
        if rank[bossB] == rank[bossA]:
            rank[bossA] += 1
    return 0


N = int(input())
arr = [input().split() for _ in range(N)]
flag = 0
rank = [0]*100
par = [0]*100
for i in range(65, 65+N):
    par[i] = i


for a, b in arr:
    if union(ord(a), ord(b)):
        flag = 1
        break

if flag == 1: print('발견')
else: print('미발견')