a=[0,0,0,1],[1,1,0,1],[1,0,0,1],[1,1,1,1]
b=[1,1,1,1],[1,0,1,1],[1,0,0,0],[1,0,0,0]
c=[[0]*4 for i in range(4)]
for i in range(4):
    for j in  range(4):
        c[i][j]=a[i][j]+b[i][j]
for i in range(4):
    for j in  range(4):
        if c[i][j]==0:
            print(f'({i},{j})')