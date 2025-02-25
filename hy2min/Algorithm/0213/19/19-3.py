def bomb(y,x):
    d_y = [1,1,1,0,0,-1,-1,-1]
    d_x = [-1,0,1,-1,1,-1,0,1]
    for i in range(8):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if 0 <= dy < 4 and 0 <= dx < 5:
            arr[dy][dx] = "#"

arr = [['_'] * 5 for _ in range(4)]
for _ in range(2):
    y, x = map(int, input().split())
    bomb(y, x)

for i in arr:
    for j in i:
        print(j, end=" ")
    print()
