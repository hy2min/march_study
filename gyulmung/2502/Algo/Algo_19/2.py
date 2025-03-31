Map =  [[3, 3, 5, 3, 1],
        [2, 2, 4, 2, 6], 
        [4, 9, 2, 3, 4],
        [1, 1, 1, 1, 1],
        [3, 3, 5, 9, 2]]

def research_map(y,x):
    re_map_Y = [1, 1, -1, -1]
    re_map_X = [1, -1, -1, 1]
    Sum = 0
    for i in range(4):
        dy = re_map_Y[i] + y
        dx = re_map_X[i] + x
        if dx < 0 or dy < 0 or dx >= 5 or dy >= 5:
            continue

        Sum += Map[dy][dx]
    return Sum

Max = -1e8
for i in range(5):
    for j in range(5):
        result = research_map(i,j)
        if Max < result:
            Max = result
            Max_y, Max_x = i, j
print(Max_y,Max_x)