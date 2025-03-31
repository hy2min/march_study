A=[list(map(int,input().split())) for _ in range(4)]
blank=list(input())
B=[list(map(int,input().split())) for _ in range(4)]

flag=0
for i in range(4):
    for j in range(4):
        if A[i][j] ==1 and B[i][j] == 1:
            flag=1
            break
    if flag:
        break

if flag:
    print('걸리다')
else:
    print('걸리지않는다')