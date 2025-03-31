import sys
sys.stdin = open('input.txt', 'r')

def shrimp(y, x):
    for i in range(4):
        for j in range(1, 3):
            dy = diry[i]*j+y
            dx = dirx[i]*j+x
            if dy < 0 or dx < 0 or dy >= 7 or dx >= 7: continue
            if arr[dy][dx] == '1':
                return False
    return True

def squid(y, x):
    for i in range(4):
        for j in range(1, 4):
            dy = diry[i]*j+y
            dx = dirx[i]*j+x
            if dy < 0 or dx < 0 or dy >= 7 or dx >= 7: continue
            if arr[dy][dx] == '2':
                return False
    return True


diry = [0, 0, 1, -1]
dirx = [1, -1, 0, 0]
arr = [list(input()) for _ in range(7)]
Flag = True
for i in range(7):
    for j in range(7):
        if arr[i][j] == '1':
            Flag = shrimp(i, j)
            if not Flag:
                break
        if arr[i][j] == '2':
            Flag = squid(i, j)
            if not Flag:
                break
    if not Flag:
        break

if Flag:
    print('pass')
else:
    print('fail')