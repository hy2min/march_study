arr = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

count = 2

for i in range(4):
    for j in range(4):
        arr[j][i] = count
        count += 2

for i in arr:
    for j in i:
        print(j,end = ' ')
    print()