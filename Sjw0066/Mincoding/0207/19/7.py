vect = [[0]*3 for _ in range(4)]


for i in range(4):
    y,x=map(int,input().split())
    vect[y][x] = 5

for i in vect:
    for j in i :
        print(j,end=" ")
    print()


