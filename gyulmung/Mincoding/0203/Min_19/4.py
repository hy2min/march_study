lst = []
vect = [[0]*3 for _ in range(4)]

for i in range(4):
    arr = []
    for j in range(1):
        y, x = map(int, input().split())
        arr.append(y)
        arr.append(x)
    lst.append(arr)

for i in range(4):
    vect[lst[i][0]][lst[i][1]] = 5

for i in range(4):
    for j in range(3):
        print(vect[i][j], end = ' ')
    print()


