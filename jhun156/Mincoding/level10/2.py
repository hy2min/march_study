arr = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

a = int(input())
count = 1
if a % 2 == 0:
    for i in range(4):
        arr[i][i] = count
        count += 1
else:
    for i in range(4):
        arr[i][3-i] = count
        count += 1

for i in range(4):
    for j in range(4):
        print(arr[i][j], end = ' ')
    print()