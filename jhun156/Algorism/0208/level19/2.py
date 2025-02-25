map = [
    [3,3,5,3,1],
    [2,2,4,2,6],
    [4,9,2,3,4],
    [1,1,1,1,1],
    [3,3,5,9,2],
]

directX = [1,1,-1,-1]
directY = [1,-1,1,-1]

Max = 0
y,x = 0,0

def find_Max(Y,X):
    result = 0
    for i in range(4):
        dx = X + directX[i]
        dy = Y + directY[i]
        if 0 <= dx <= 4 and 0 <= dy <= 4:
            result += map[dy][dx]
    return result

for i in range(5):
    for j in range(5):
        ret = find_Max(i,j)
        if Max < ret:
            Max = ret
            y,x = i,j

print(y,x)