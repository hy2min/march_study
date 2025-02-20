arr = [list(map(int, input().split())) for _ in range(4)]
y1, x1 = 3, 4
y2, x2 = 0, 0
for i in range(4):
    for j in range(5):
        if arr[i][j]:
            y1 = min(y1, i)
            x1 = min(x1, j)
            y2 = max(y2, i)
            x2 = max(x2, j)
print(f'({y1},{x1})')
print(f'({y2},{x2})')
