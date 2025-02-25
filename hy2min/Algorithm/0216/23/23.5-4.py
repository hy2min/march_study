def change(y, x):
    for t in range(4):
        if arr[y][x] == lst[t]:
            if t == 3:
                arr[y][x] = lst[0]
            else:
                arr[y][x] = lst[t+1]
            return

arr = [
    [3,5,4,1],
    [1,1,2,3],
    [6,7,1,2]
]

lst = list(map(int, input().split()))

for i in range(3):
    for j in range(4):
        change(i,j)

for i in arr:
    print(*i)