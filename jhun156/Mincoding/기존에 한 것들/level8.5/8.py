arr = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

a,b = map(int,input().split())

for i in range(3):
    for j in range(3):
        arr[i][j] = a

for i in range(3,6):
    for j in range(3):
        arr[i][j] = b
    
for i in range(6):
    for j in range(3):
        print(arr[i][j],end='')
    print()
