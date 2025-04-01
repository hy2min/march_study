arr = [[12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]

num = int(input())

if num == 1:
    for i in range(4):
        arr[0][i] = 7
elif num == 2:
    for i in range(4):
        arr[1][i] = 7
elif num == 3:
    for i in range(4):
        arr[2][i] = 7

for i in range(3):
    for j in range(4):
        print(arr[i][j], end = " ")
    print()
