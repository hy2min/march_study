arr = [
    [0,0,0,0,0,0,0],
    [0,0,1,0,1,0,0],
    [0,1,2,0,2,1,0],
    [0,0,1,2,1,0,0],
    [0,0,2,1,0,1,0],
    [0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0],
]

y,x = map(int,input().split())

def find_black(y,x):
    cnt = 0
    directY = [0,0,1,-1]
    directX = [1,-1,0,0]
    for i in range(4):
        dy = y + directY[i]
        dx = x + directX[i]
        if dy < 0 or dy > 6 or dx < 0 or dx > 6:
            continue
        if arr[dy][dx] == 2:
            cnt += 1

    return cnt

ans = find_black(y,x)
print(ans)