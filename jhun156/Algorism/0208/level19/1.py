arr = [
    [3,5,4],
    [1,1,2],
    [1,3,9],
]

y,x = map(int,input().split())

directX = [0,0,-1,1]
directY = [-1,1,0,0]
Sum = 0
for i in range(4):
    dx = x + directX[i]
    dy = y + directY[i]
    if dx < 0 or dx > 2 or dy < 0 or dy > 2:
        continue
    Sum += arr[dy][dx]
print(Sum)