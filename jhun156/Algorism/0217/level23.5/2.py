arr = [[0] * 4 for _ in range(3)]
lst = []

for i in range(3):
    y,x = map(int,input().split())
    arr[y][x] = '#'
    row = [y,x]
    lst.append(row)

def find(y,x):
    directY = [0,0,1,-1]
    directX = [1,-1,0,0]
    for i in range(4):
        for j in range(1,4):
            dy = y + directY[i] * j
            dx = x + directX[i] * j
            if dy < 0 or dy > 2 or dx < 0 or dx > 3:
                break
            if arr[dy][dx] == '#':
                return 1
    return 0


for i in range(3):
    ans = find(lst[i][0],lst[i][1])
    if ans == 1:
        print("위험")
        break
else:
    print("안전")
