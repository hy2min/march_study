lst = []

for i in range(4):
    arr = [i for i in map(int,input().split())]
    lst.append(arr)

for i in range(4):
    for j in range(4):
        if lst[i][j] == 0:
            lst[i][j] = '!'
        elif lst[i][j] % 2 == 0:
            lst[i][j] = '#'
        else:
            lst[i][j] = '@'

for i in range(4):
    for j in range(4):
        print(lst[i][j],end='')
    print()