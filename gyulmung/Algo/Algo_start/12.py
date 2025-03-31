num = int(input())

arr = [[0]*4 for _ in range(4)]
count = 0
for i in range(4):
    if i  < 3:
        for j in range(4):
            arr[i][j] = num + count
            count += 1
    elif i == 3:
        for j in range(3, -1, -1):
            arr[i][j] = num + count
            count += 1

for i in range(4):
    for j in range(4):
        print(arr[i][j], end = " ")
    print()