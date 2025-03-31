# import sys
# sys.stdin = open("input.txt", "r")

arr = [list(map(int,input().split())) for _ in range(5)]
check = [list(map(int,input().split())) for _ in range(5)]

def find(num,y,x):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                arr[i][j] = 'X'
                return i,j

def bingo():
    ret = 0         # 리턴할 값

    y,x = 0,0       # 좌표 초기화
    directY = [1,1,0]
    directX = [0,1,1]
    for i in range(3):
        cnt = 0
        for j in range(5):
            dy = y + directY[i] * j
            dx = x + directX[i] * j
            if arr[dy][dx] == 'X':
               cnt += 1
            else:
                break
        if cnt == 5:
            ret += 1

    y,x = 4,0
    directY = [-1,0]
    directX = [1,1]
    for i in range(2):
        cnt = 0
        for j in range(5):
            dy = y + directY[i] * j
            dx = x + directX[i] * j
            if arr[dy][dx] == 'X':
               cnt += 1
            else:
                break
        if cnt == 5:
            ret += 1

    x = 0
    directX = 1
    directY = 0
    for y in range(1,4):
        cnt = 0
        for i in range(5):
            dy = y + directY * i
            dx = x + directX * i
            if arr[dy][dx] == 'X':
                cnt += 1
            else:
                break
        if cnt == 5:
            ret += 1

    y = 0
    directX = 0
    directY = 1
    for x in range(1,5):
        cnt = 0
        for i in range(5):
            dy = y + directY * i
            dx = x + directX * i
            if arr[dy][dx] == 'X':
                cnt += 1
            else:
                break
        if cnt == 5:
            ret += 1

    return ret


ans = 0
ret = 0
for i in range(5):
    for j in range(5):
        ans += 1
        Y,X = find(check[i][j],i,j)
        ret = bingo()
        if ret >= 3:
            break
    if ret >= 3:
        break
print(ans)