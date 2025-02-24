arr = [['_']* 4 for _ in range(4)]

for _ in range(3):
    y,x = map(int, input().split())
    arr[y][x] = '#'

    directy = [-1,-1,-1,0,0,1,1,1]
    directx = [-1,0,1,-1,1,-1,0,1]
    for i in range(8):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy < 0 or dx < 0 or dy >= 4 or dx >=4:
            continue
        if arr[dy][dx] == '#':
            continue
        arr[dy][dx] = '@'

for i in arr:
    for j in i:
        print(j,end="")
    print()