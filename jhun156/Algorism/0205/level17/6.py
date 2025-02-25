mask1 = [
    [0,0,0,1],
    [1,1,0,1],
    [1,0,0,1],
    [1,1,1,1],
]

mask2 = [
    [1,1,1,1],
    [1,0,1,1],
    [1,0,0,0],
    [1,0,0,0],
]

for i in range(4):
    for j in range(4):
        if mask1[i][j] == 1 or mask2[i][j] == 1:
            mask1[i][j],mask2[i][j] = 1,1

for i in range(4):
    for j in range(4):
        if mask1[i][j] == 0:
            print(f"({i},{j})")