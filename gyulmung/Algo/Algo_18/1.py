arr = [[65000, 35, 42, 70], [70, 35, 65000, 1300], [65000, 30000, 38, 42]]
len = [0]*65535
Max = 0

for i in range(3):
    for j in range(4):
        len[arr[i][j]] += 1
        if Max < len[arr[i][j]]:
            Max = arr[i][j]

print(Max)
