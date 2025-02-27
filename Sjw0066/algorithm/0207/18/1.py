dat=[0]*65001
arr=[[65000,35,42,70],[70,35,65000,1300],[65000,30000,38,42]]

for i in arr:
    for j in i:
        dat[j]+=1

ans=dat.index(max(dat))

print(ans)


