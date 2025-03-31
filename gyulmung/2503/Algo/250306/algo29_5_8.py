arr = [list(input()) for _ in range(4)]
route = []
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            a=[(i, j)]
        elif arr[i][j] == 'C':
            c=[(i, j)]
        elif arr[i][j] == 'D':
            d=[(i, j)]

diy = [0, 1, 0, -1, 0]
dix = [1, 0, -1, 0, 1]
for i in range(5):
    # A 일때
    dy = diy[i] + a[i][0]
    dx = dix[i] + a[i][1]
    if dy < 0 or dx < 0 or dy > 3 or dx > 2:
        a.append((a[i][0], a[i][1]))
        pass
    if arr[dy][dx] != '_':
        a.append((a[i][0], a[i][1]))
    else:
        arr[dy][dx] = 'A'
        arr[a[i][0]][a[i][1]] = '_'
        a.append((dy, dx))
    # C 일때
    dy = diy[i] + c[i][0]
    dx = dix[i] + c[i][1]
    if dy < 0 or dx < 0 or dy > 3 or dx > 2:
        c.append((c[i][0], c[i][1]))
        pass
    if arr[dy][dx] != '_':
        c.append((c[i][0], c[i][1]))
    else:
        arr[dy][dx] = 'C'
        arr[c[i][0]][c[i][1]] = '_'
        c.append((dy, dx))
    # D 일때
    dy = diy[i] + d[i][0]
    dx = dix[i] + d[i][1]
    if dy < 0 or dx < 0 or dy > 3 or dx > 2:
        d.append((d[i][0], d[i][1]))
        pass
    if arr[dy][dx] != '_':
        d.append((d[i][0], d[i][1]))
    else:
        arr[dy][dx] = 'D'
        arr[d[i][0]][d[i][1]] = '_'
        d.append((dy, dx))
print(arr)