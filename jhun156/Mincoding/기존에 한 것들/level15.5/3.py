arr = [[0] * 4 for _ in range(3)]
num = 1

for i in range(2,-1,-1):
    for j in range(3,-1,-1):
        arr[i][j] = num
        num += 1

a = int(input())

if a == 1:
    for i in range(4):
        arr[0][i] = 7
elif a == 2:
    for i in range(4):
        arr[1][i] = 7
elif a == 3:
    for i in range(4):
        arr[2][i] = 7

for i in range(3):
    print(*arr[i])