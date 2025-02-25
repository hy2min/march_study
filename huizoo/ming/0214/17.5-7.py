levelTable = [
    [10, 20],
    [30, 60],
    [100,150],
    [200,300],
]
kcals = list(map(int, input().split()))
lev = [0, 0, 0, 0]
for kcal in kcals:
    for i in range(4):
        if levelTable[i][0] <= kcal <= levelTable[i][1]:
            lev[i] += 1
for i in range(4):
    print(f'lev{i}:{lev[i]}')