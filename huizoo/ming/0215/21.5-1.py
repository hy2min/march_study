arr = [list(input()) for _ in range(4)]
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            y1, x1 = i, j
        elif arr[i][j] == 'B':
            y2, x2 = i, j
print(abs(y1-y2)+abs(x1-x2))