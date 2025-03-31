pattern = [
    (0,1),
    (1,0),
    (0,-1),
    (-1,0),
    (0,1)
]
arr = [list(input()) for _ in range(4)]


def dfs(y,x,idx,char):
    if idx == 5:
        return
    dy = y + pattern[idx][0]
    dx = x + pattern[idx][1]
    if 0 <= dy <4 and 0 <= dx < 3:
        if arr[dy][dx] == "_":
            arr[dy][dx] = char 
            arr[y][x] = '_'
            dfs(dy, dx, idx+1, char)
    else:
        dfs(y,x,idx+1,char)
for i in range(4):
    for j in range(3):
        if arr[i][j].isalpha():
            char = arr[i][j]
            dfs(i,j,0,char)

for row in arr:
    print("".join(row))
