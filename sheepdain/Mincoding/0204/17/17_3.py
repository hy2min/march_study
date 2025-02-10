arr=[3,5,9],[4,2,1],[1,1,5]
beat=[]
for i in range(3):
    beat.append(list(map(int,input().split())))
SUM=0
for i in range(3):
    for j in range(3):
        if beat[i][j]==1:
            SUM+=arr[i][j]
print(SUM)