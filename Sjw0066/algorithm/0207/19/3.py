Map=[['_']*5 for _ in range(4)]

def explode(y,x):
    global Map
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0 :
                continue
            ny=y+i
            nx=x+j
            if ny>3 or ny<0 or nx>4 or nx<0:
                continue
            Map[ny][nx] = '#'

for i in range(2):
    y,x=map(int,input().split())
    explode(y,x)

for i in Map:
    for j in i:
        print(j,end=" ")
    print()

