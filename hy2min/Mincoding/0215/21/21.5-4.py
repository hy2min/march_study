arr = [list(input()) for _ in range(4)]


for j in range(3):
    bottom = 3
    for i in range(3,-1,-1):
        if arr[i][j] != '_':
            temp = arr[i][j]
            arr[i][j], arr[bottom][j] = arr[bottom][j], arr[i][j]
            bottom -= 1

for i in arr:
    for j in i:
        print(j, end="")
    print()