def rectSum(y, x):
    dy = [0, 0, 0, 1, 1, 1]
    dx = [0, 1, 2, 0, 1, 2]
    Sum = 0
    for i in range(6):
        ny, nx = y+dy[i], x+dx[i]
        Sum += image[ny][nx]
    return Sum

image = [list(map(int, input().split())) for _ in range(4)]
Max = 0
y1, x1 = 0, 0
for i in range(3):
    for j in range(2):
        ret = rectSum(i, j)
        if Max < ret:
            Max = ret
            y1, x1 = i, j

print(f'({y1},{x1})')