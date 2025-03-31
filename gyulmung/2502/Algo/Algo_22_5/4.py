a, b = map(int, input().split())
arr = [[[0]*3 for _ in range(2)] for _ in range(3)]

def abc(lev, y, x):
    global arr
    if lev == 3:
        return

    for i in range(2):
        for j in range(3):
            if i == 0:
                arr[lev][i][j] = y
            else:
                arr[lev][i][j] = x

    abc(lev + 1, y, x)

abc(0, a, b)

for i in arr:
    for j in i:
        print(*j)
    print()
