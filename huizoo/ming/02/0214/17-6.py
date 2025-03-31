arr = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1],
]
arr2 = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
]
arr3 = [[0]*4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        arr3[i][j] = max(arr2[i][j], arr[i][j])
        if arr3[i][j] == 0:
            print(f'({i},{j})')
