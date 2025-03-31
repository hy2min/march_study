go = [[0,0,0,0,0,0,0],
      [0,0,1,0,1,0,0],
      [0,1,2,0,2,1,0],
      [0,0,1,2,1,0,0],
      [0,0,2,1,0,1,0],
      [0,1,1,0,0,0,0],
      [0,0,0,0,0,0,0]]

a, b = map(int, input().split())

def delete_go(y, x):
    diry = [0, 0, 1, -1]
    dirx = [1, -1, 0, 0]
    cnt = 0
    for i in range(4):
        dy = diry[i] + y
        dx = dirx[i] + x
        if dy < 0 or dx < 0 or dy > 6 or dx > 6:
            continue
        if go[dy][dx] == 1:
            cnt += 1
    if cnt == 4:
        return 1
    else: return 0

go[a][b] = 1
result = 0
for i in range(7):
    for j in range(7):
        if go[i][j] == 2:
            result += delete_go(i,j)

print(result)