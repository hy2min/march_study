Map = [
    ['_','_','_','_','_'],
    ['_','_','_','_','_'],
    ['_','_','_','_','_'],
    ['_','_','_','_','_'],
]

YX_list = []
for i in range(2):
    YX_list.extend(map(int,input().split()))

directX = [0,0,1,-1,1,1,-1,-1]
directY = [1,-1,0,0,1,-1,1,-1]

def Bomb(y,x):
    for i in range(8):
        dy = y + directY[i]
        dx = x + directX[i]
        if 0 <= dy <= 3 and 0 <= dx <= 4:
            Map[dy][dx] = '#'

for i in range(0,4,2): 
    Bomb(YX_list[i],YX_list[i+1]) # Y, X 좌표 2번 반복

for i in range(4):
    print(*Map[i])