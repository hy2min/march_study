arr = [list(input()) for _ in range(4)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


arr2 = []


for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A' or arr[i][j] == 'C' or arr[i][j] == 'D' or arr[i][j] == 'H':
            arr2.append((arr[i][j], i, j))

for i in range(5):
    for j, (name, y, x) in enumerate(arr2):
        dy, dx = directions[i%4]
        ny, nx = y+dy, x+dx

        if 0 <= ny < 4 and 0 <= nx < 3 and arr[ny][nx] == '_':  # 범위 내이고 빈 공간('_')일 때

            arr[ny][nx] = name
            arr[y][x] = '_'
            arr2[j] = (name, ny, nx)

for i in range(4):
    for j in range(3):
        print(arr[i][j],end='')
    print()