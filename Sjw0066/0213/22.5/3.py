n=input()
arr=[[[0]*3 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        for k in range(3):
            arr[i][j][k] = chr(ord(n)+i)

for i in range(3):
    for j in range(3):
        for k in range(3):
            print(arr[i][j][k],end="")
        print()
    print()

