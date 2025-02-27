levelTable=[[10,20],[30,60],[100,150],[200,300]]

fruit=list(map(int,input().split()))

cnt={}
for i in fruit:
    for j in range(4):
        cnt.setdefault(j,0)
        if levelTable[j][0]<= i <=levelTable[j][1]:
                cnt[j]+=1

for i in range(4):
    print(f'lev{i}:{cnt[i]}')



