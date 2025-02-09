cell=[list(map(int,input().split())) for _ in range(5)]


def check_cell(y,x):
    for i in range(-1,2):
        for j in range(-1,2):
            ny=y+i
            nx=x+j
            if i==0 and j==0 :
                continue
            if ny>4 or ny<0 or nx>3 or nx<0:
                continue
            if  cell[ny][nx] == 1:
                return False
    return True

for i in range(5):
    for j in range(4):
        flag=check_cell(i,j)

if flag:
    print('안정된 상태')
else:
    print("불안정한 상태")