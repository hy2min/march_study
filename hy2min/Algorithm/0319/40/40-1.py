arr = [list(map(int, input().split())) for _ in range(4)]

accu = [[0] * 4 for _ in range(4)]

for i in range(2, -1, -1):
    accu[i][3] = accu[i+1][3] + arr[i][3]
    accu[3][i] = accu[3][i+1] + arr[3][i]

for i in range(2, -1 ,-1):
    for j in range(2, -1, -1):
        down = accu[i+1][j]
        right = accu[i][j+1]

        if down > right:
            accu[i][j] = arr[i][j] + right
        else:
            accu[i][j] = arr[i][j] + down

y, x = 0, 0  # 출발
route = [(y, x)]

while (y, x) != (3, 3):  # 도착 breakpoint
    if y == 3:
        x += 1
    elif x == 3:
        y += 1

    else:
        if accu[y+1][x] > accu[y][x+1]:
            x += 1
        else:
            y += 1

    route.append((y,x))

for y, x in route:
    print(f'{y},{x}')