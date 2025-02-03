arr = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]
count = 1

for i in range(4):
    for j in range(4):
        arr[j][3-i] = count
        count += 1

for i in range(4):
    for j in range(4):
        print(arr[i][j],end = ' ')
    print()

