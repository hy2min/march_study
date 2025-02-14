rect = [[0]*4 for _ in range(4)]

lst = [list(map(str, input().split())) for _ in range(3)]

for i in range(3):
    lst[i][1] = int(lst[i][1])
    if lst[i][0] == 'G':
        for j in range(4):
            rect[lst[i][1]][j] = 1
    if lst[i][0] == 'S':
        for j in range(4):
            rect[j][lst[i][1]] = 1

for i in range(4):
    for j in range(4):
        print(rect[i][j], end = ' ')
    print()