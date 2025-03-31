arr=[[3,1,9],[7,2,1],[1,0,8]]

masking=[list(map(int,input().split())) for _ in range(3)]

flag=0

for i in range(3):
    for j in range(3):
        if masking[i][j]==0:
            arr[i][j]=0
        if 3<= arr[i][j] <=5:
            flag=1

if flag :
    print("발견")
else:
    print('미발견')
