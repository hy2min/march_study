arr = [list(input()) for _ in range(4)]
A = []
C = []
D = []
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            A.extend((i,j))
            break
        elif arr[i][j] == 'C':
            C.extend((i,j))
            break
        elif arr[i][j] == 'D':
            D.extend((i,j))
            break

directY = [0,1,0,-1]
directX = [1,0,-1,0]
cnt = 0

while cnt < 5:
    now_y,now_x = directY.pop(0),directX.pop(0)
    if A[0]+now_y >= 0 and A[0]+now_y <= 3 and A[1]+now_x >= 0 and A[1]+now_x <= 2 and arr[A[0]+now_y][A[1]+now_x] == '_':
        arr[A[0]][A[1]],arr[A[0]+now_y][A[1]+now_x] = arr[A[0]+now_y][A[1]+now_x],arr[A[0]][A[1]]
        A[0] = A[0]+now_y
        A[1] = A[1]+now_x
    if C[0]+now_y >= 0 and C[0]+now_y <= 3 and C[1]+now_x >= 0 and C[1]+now_x <= 2 and arr[C[0]+now_y][C[1]+now_x] == '_':
        arr[C[0]][C[1]],arr[C[0]+now_y][C[1]+now_x] = arr[C[0]+now_y][C[1]+now_x],arr[C[0]][C[1]]
        C[0] = C[0] + now_y
        C[1] = C[1] + now_x
    if D[0]+now_y >= 0 and D[0]+now_y <= 3 and D[1]+now_x >= 0 and D[1]+now_x <= 2 and arr[D[0]+now_y][D[1]+now_x] == '_':
        arr[D[0]][D[1]],arr[D[0]+now_y][D[1]+now_x] = arr[D[0]+now_y][D[1]+now_x], arr[D[0]][D[1]]
        D[0] = D[0] + now_y
        D[1] = D[1] + now_x
    directY.append(now_y)
    directX.append(now_x)
    cnt += 1

for i in range(4):
    for j in range(3):
        print(arr[i][j],end='')
    print()


