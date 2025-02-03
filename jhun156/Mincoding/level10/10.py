a = int(input())

arr = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]
count = 1

for i in range(3):
    for j in range(4):
        arr[2-i][3-j] = count
        count += 1

for i in range(3):
    arr[i][a] = 0

for i in range(3):
    for j in range(4):
        print(arr[i][j], end = ' ')
    print()