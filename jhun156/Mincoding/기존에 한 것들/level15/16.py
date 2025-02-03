arr = [[0] * 3 for _ in range(3)]

a = input()
A = ord(a)

i = 2

while i >= 0:
    j = 0
    while i + j <= 2:
        arr[i][j] = chr(A)
        A += 1
        j += 1
    i -= 1

for i in range(3):
    for j in range(3):
        if arr[i][j] == 0:
            print(" ",end='')
        else:
            print(arr[i][j],end='')
    print()
