import sys
sys.stdin = open("input.txt","r")

T=int(input())
def findboss(member):

    if parent[member] == member:
        return member

    ret=findboss(parent[member])
    parent[member]=ret
    return ret


def union(a,b):
    global flag
    bossA,bossB=findboss(a),findboss(b)

    if bossA==bossB:
        flag=0
        return

    parent[bossB]=bossA
    flag=1



for tc in range(1,T+1):
    V,E = map(int,input().split())
    arr=[]
    parent = list(range(V+1))
    total=0

    for i in range(E):
        flag=0
        a,b,c=map(int,input().split())
        arr.append((a,b,c))

    arr.sort(key=lambda x:x[2])

    for i in range(E):
        union(arr[i][0],arr[i][1])

        if flag:
            total+=arr[i][2]

    print(f'#{tc} {total}')


