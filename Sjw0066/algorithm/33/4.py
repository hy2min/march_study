N,K=map(int,input().split())
name=[0]*(K+1)
arr=[[] for _ in range(K+1)]
boss=[-1]*(K+1)

def union(a,b):

    bossA,bossB=findboss(a),findboss(b)

    if bossA==bossB:
        return

    boss[b]=bossA

def findboss(member):

    if boss[member] == -1:
        return member
    ret = findboss(boss[member])
    boss[member] = ret
    return ret


for i in range(N):
    a,b=input().split()
    if a.isdecimal() and b.isdecimal():
        arr[int(a)].append(int(b))
        union(int(a),int(b))
    else:
        if a.isdecimal():
            name[int(a)]=b
        else:
            name[int(b)]=a

flag=1
while flag:
    flag=0
    for i in range(1,len(name)):
        if not name[i]:
            flag=1
            name[i] = name[boss[i]]

name.pop(0)
print(*name,sep="")


