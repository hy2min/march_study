arr = [[[0] * 3 for _ in range(3)] for _ in range(3)]

a = input()
A = ord(a)

for i in range(3):
    for j in range(3):
        for k in range(3):
            arr[i][j][k] = chr(A+i)
            print(arr[i][j][k],end='')
        print()
    print()