Map=[list(input()) for _ in range(4)]


def abc(level):

    if level==5:
        return

    for i in range(3):
        y=monster[i][0]
        x=monster[i][1]
        ny=direct_y[level%4]+y
        nx=direct_x[level%4]+x
        if ny>3 or ny<0 or nx<0 or nx>2:
            continue
        if Map[ny][nx] != '_':
            continue
        Map[ny][nx] , Map[y][x] = Map[y][x] , Map[ny][nx]
        monster[i][0] = ny
        monster[i][1] = nx

    abc(level+1)


index=dict()
for i in range(4):
    for j in range(3):
        if Map[i][j] != '#' and Map[i][j] != '_':
            index[Map[i][j]] = [i,j]

col_row=sorted(list(index.items()),key=lambda x:x[0])
monster=[]

for i in range(len(col_row)):
    monster.append(col_row[i][1])

direct_y=[0,1,0,-1]
direct_x=[1,0,-1,0]

abc(0)

for i in Map:
    for j in i :
        print(j,end="")
    print()




