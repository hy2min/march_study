image = [list(map(int, input().split())) for _ in range(4)]
max_total = 0
max_y = -1
max_x = -1
def rectSum(y,x):
    total = 0
    for i in range(y, y+2):
        for j in range(x, x+3):
            total += image[i][j]

    return total

for y in range(3):
    for x in range(2):
        if max_total < rectSum(y, x):
            max_total = rectSum(y, x)
            max_y = y
            max_x = x
print(f'({max_y},{max_x})')
