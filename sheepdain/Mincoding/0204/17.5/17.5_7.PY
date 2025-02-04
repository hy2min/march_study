levelTable=[10,20],[30,60],[100,150],[200,300]
level=list(map(int,input().split()))
lev=[0,0,0,0]
for i in level:
    for j in range(4):
        if levelTable[j][0]<=i<=levelTable[j][1]:
            lev[j]+=1
    print(lev)
for i in range(4):
    print(f"lev{i}:{lev[i]}")