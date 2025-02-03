arr = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

a = int(input())

for i in range(5):
    for j in range(5):
        arr[i][j] = a

for i in range(3):
    for j in range(3):
        arr[i+1][j+1] = 0

for i in range(5):
    for j in range(5):
        if arr[i][j] == 0:
            print("_",end='')
        else:
            print(arr[i][j],end='')
    print()