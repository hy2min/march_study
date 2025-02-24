arr = [list(input()) for _ in range(4)]
for _ in range(3):
    for i in range(3, 0, -1):
        for j in range(3):
            if arr[i][j] == '_':
                arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
print('\n'.join(''.join(row) for row in arr))