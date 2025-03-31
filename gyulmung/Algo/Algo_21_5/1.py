arr = [list(map(str, input())) for _ in range(4)]
A_y, A_x = 0, 0
B_y, B_x = 0, 0
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            A_y, A_x = i, j
        elif arr[i][j] == 'B':
            B_y, B_x = i, j
AB_y = abs(A_y - B_y)
AB_x = abs(A_x - B_x)

print(AB_y+AB_x)