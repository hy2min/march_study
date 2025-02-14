Map = [[3, 5, 1], [3, 8, 1], [1, 1, 5]]
Bitarray = [list(map(int, input().split())) for _ in range(2)]

def find_Max(y, x):
    Sum = 0
    for i in range(2):
        for j in range(2):
            dy = y + i
            dx = x + j
            
            if dy < 0 or dx < 0 or dy >= 3 or dx >= 3:
                continue
            elif Bitarray[i][j] != 0:
                Sum += Map[dy][dx]
    return Sum                



Max = -1e8
for i in range(3):
    for j in range(3):
        Sum = find_Max(i, j)
        if Max < Sum:
            Max = Sum
            y, x = i, j
print(f'({y},{x})')