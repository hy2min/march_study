N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
group=[-1]*N
flag=0

def union(a,b):
    global flag
    bossA,bossB= findboss(a),findboss(b)

    if bossA==bossB:
        flag=1
        return

    group[bossB] = bossA

def findboss(member):

    if group[member] == -1:
        return member
    ret = findboss(group[member])
    group[member] = ret
    return ret


for i in range(N):
    for j in range(i,N):
        if arr[i][j] == 1:
            union(i,j)

if flag:
    print('cycle 발견')
else:
    print('미발견')