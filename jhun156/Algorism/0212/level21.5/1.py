arr = [list(input()) for _ in range(4)]

A_Y,A_X,B_Y,B_X = 0,0,0,0

for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            A_Y,A_X = i,j
        elif arr[i][j] == 'B':
            B_Y,B_X = i,j

Y = abs(A_Y-B_Y)
X = abs(A_X-B_X)
ans = Y + X
print(ans)

