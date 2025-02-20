a, b = map(int, input().split())

arr = [[[0]*3 for _ in range(2)] for _ in range(3)]

def abc(level):
    if level == 3:
         return

    for i in range(3):
        arr[level][0][i] = a
        arr[level][1][i] = b

    abc(level+1)

abc(0)

for i in range(3):
    for j in range(2):
        print(*arr[i][j])
    print()