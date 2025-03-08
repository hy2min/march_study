import copy
arr = [list(input()) for _ in range(4)]
N = int(input())
d = [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]
boomed = [[0]*4 for _ in range(4)]
enemys = []
for i in range(4):
    for j in range(4):
        if arr[i][j] != '_':
            enemys.append((i, j, arr[i][j]))

path = []
Max = 0
target = []
def dfs(level):
    global Max, target, boomed
    if level == N:
        cnt = 0
        for row in boomed:
            cnt += row.count(1)
        if Max < cnt:
            Max = cnt
            target = path[:]
        return

    for enemy in enemys:
        y, x, alp = enemy
        if not boomed[y][x]:
            boomed2 = copy.deepcopy(boomed)
            for dy, dx in d:
                ny, nx = y+dy, x+dx
                if 0<=ny<4 and 0<=nx<4:
                    if arr[ny][nx] != '_':
                        boomed[ny][nx] = 1
            path.append(alp)
            dfs(level+1)
            boomed = copy.deepcopy(boomed2)
            path.pop()

dfs(0)
print(*sorted(target))