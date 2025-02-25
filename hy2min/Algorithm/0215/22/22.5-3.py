arr = [[[0] * 3 for _ in range(3)] for _ in range(3)]
s = input()
s = ord(s)
def abc(level,s):
    if level == 3:
        return

    for i in range(3):
        for j in range(3):
            arr[level][i][j] = chr(s)
    abc(level+1, s+1)
abc(0,s)


for i in range(3):
    for j in range(3):
        for k in range(3):
            print(arr[i][j][k], end="")
        print()
    print()