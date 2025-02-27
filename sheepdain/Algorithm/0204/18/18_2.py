arr=[]
for i in range(3):
    arr.append(list(map(int,input().split())))

DAT=[0]*10
for i in arr:
    for j in i:
        DAT[j]+=1
for i in range(1,10):
    if DAT[i]==0:
        print(i,end=' ')