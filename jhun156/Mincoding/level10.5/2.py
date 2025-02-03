arr = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

count = 1

for i in range(5):
    for j in range(5):
        arr[j][4-i] = count
        count += 1

a = int(input())

for i in range(5):
    arr[a][i] = a

for i in arr:
    for j in i:
        print(j, end= ' ')
    print()