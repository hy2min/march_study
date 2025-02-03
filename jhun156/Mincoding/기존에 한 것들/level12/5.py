a = int(input())

arr = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

start_index = 2

for i in range(3):
    for j in range(start_index,4):
        arr[i][j] = a
        a += 1
    start_index -= 1

for i in arr:
    for j in i:
        if j == 0:
            print(" ", end = '')
        else:
            print(j, end = '')
    print()
