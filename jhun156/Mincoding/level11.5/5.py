arr = [
    [0,0,0],
    [0,0,0],
]

lst = [i for i in map(int,input().split())]
count = 0

for i in range(2):
    for j in range(3):
        arr[i][j] = lst[count]
        count += 1

for i in range(2):
    for j in range(3):
        if arr[i][j] == 0:
            arr[i][j] = '#'
        print(arr[i][j],end='')
    print()
