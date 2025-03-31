arr = [list(map(str, input())) for _ in range(4)]

def abc(y, x):
    global Max_y
    if y+1 > 3: return
    if arr[y+1][x] == '_':
        Max_y = max(Max_y, y+1)
        abc(y+1, x)
    else:
        return



for i in range(3, -1, -1):
    for j in range(3):
        Max_y = 0
        if arr[i][j] != '_' and i + 1 <= 3:
            abc(i, j)
            arr[Max_y][j], arr[i][j] = arr[i][j], arr[Max_y][j]
for i in range(4):
    for j in range(3):
        print(arr[i][j],end = '')
    print()

