arr1 = [
    [0,0,0,1],
    [1,1,0,1],
    [1,0,0,1],
    [1,1,1,1],
]

arr2 = [
    [1,1,1,1],
    [1,0,1,1],
    [1,0,0,0],
    [1,0,0,0],
]

arr3 = [[0] * 4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        if arr1[i][j] == 1 or arr2[i][j] == 1:
            arr3[i][j] = 1


for i in range(4):
    for j in range(4):
        if arr3[i][j] == 0:
            pass
            print(f'({i},{j})')