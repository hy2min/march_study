from collections import deque
arr=[list(map(int,input().split())) for _ in range(4)]
result=[[21e8]*4 for _ in range(4)]
result[0][0] = 0
result[3][3] = 0

for i in range(2,-1,-1):
    result[i][3] = result[i+1][3] + arr[i][3]
    result[3][i] = result[3][i+1] + arr[3][i]

for i in range(2,-1,-1):
    for j in range(2,-1,-1):
        right=result[i][j+1]
        down=result[i+1][j]

        val=0
        if down>right:
            val=right + arr[i][j]
        else:
            val=down + arr[i][j]

        result[i][j] = val

q=deque()
q.append((0,0))
direct_y=[1,0]
direct_x=[0,1]

while q:
    Min=21e8
    miny=0
    minx=0

    y,x=q.popleft()
    print(f'{y},{x}')
    if y==3 and x==3:
        break
    for i in range(2):
        dy=direct_y[i]+y
        dx=direct_x[i]+x
        if dy>3 or dx>3 : continue
        ret=result[dy][dx]
        if Min>ret:
            Min=ret
            miny=dy
            minx=dx
        else:
            continue

    q.append((miny,minx))