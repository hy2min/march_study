arr=[
    [0,0,0,0,0,0,0],
    [0,0,1,0,1,0,0],
    [0,1,2,0,2,1,0],
    [0,0,1,2,1,0,0],
    [0,0,2,1,0,1,0],
    [0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0],
]

a,b=map(int,input().split())

def check_block(y,x):
    cnt=0
    direct_y=[0,0,1,-1]
    direct_x=[1,-1,0,0]
    for i in range(4):
        ny=direct_y[i]+y
        nx=direct_x[i]+x
        if ny<0 or ny>6 or nx<0 or nx>6:
            continue
        if arr[ny][nx] == 1:
            cnt+=1

    if cnt == 4:
        return 1
    else:
        return 0

arr[a][b] = 1

answer=0
for i in range(7):
    for j in range(7):
        answer+=check_block(i,j)
print(answer)

