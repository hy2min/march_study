lst = []
for i in range(5):
    row = list(map(int,input().split()))
    lst.append(row)

directX = [0,0,-1,1,1,1,-1,-1]
directY = [-1,1,0,0,1,-1,1,-1]

def check(y,x):
    if lst[y][x] == 0:
        return 0
    else:
        for i in range(8):
            dy = y + directY[i]
            dx = x + directX[i]
            if 0 <= dx <= 3 and 0 <= dy <= 4:
                if lst[dy][dx] == 1:
                    return 1
result = True
for i in range(5):
    for j in range(4):
        ans = check(i,j)
        if ans == 1:
            result = False
            break
if result:
    print("안정된 상태")
else:
    print("불안정한 상태")