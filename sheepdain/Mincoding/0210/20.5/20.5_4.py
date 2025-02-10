def ischeck(i,j):
    if (A[i][j] and B[i][j])==1:
            print('걸리다')
            return

A=[list(map(int,input().split())) for i in range(4)]
Z=input()
B=[list(map(int,input().split())) for i in range(4)]
ret=0
for i in range(4):
    for j in range(4):
        if (A[i][j] and B[i][j])==1:
            ret=1
            print('걸리다')
            break
    if ret==1:
         break
if ret==0:
    print('걸리지않는다')