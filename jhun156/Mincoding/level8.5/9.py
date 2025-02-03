a,b = input().split()

arr = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]

for i in range(3):
    for j in range(4):
        arr[i][j] = a

for i in range(3):
    for j in range(4,6):
        arr[i][j] = b

for i in range(3):
    for j in range(6):
        print(arr[i][j],end='')
    print()