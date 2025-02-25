arr = [[0] * 4 for _ in range(4)]

a = int(input())

for i in range(4):
    for j in range(4):
        if i % 2 == 0:
            arr[i][j] = a
            a += 1
        else:
            arr[i][3-j] = a
            a += 1
for i in range(4):
    print(*arr[i])