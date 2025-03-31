T=int(input())

def findboss(member):

    if parents[member]==member:
        return member

    ret=findboss(parents[member])
    parents[member]=ret
    return ret




def union(a,b):

    bossA,bossB=findboss(a),findboss(b)

    if bossA==bossB:
        return

    parents[bossB]=bossA



for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=list(map(int,input().split()))
    parents=list(range(N+1))

    for i in range(M):
        union(arr[2*i],arr[2*i+1])

    temp=[0]*N
    for i in range(1,N+1):
        temp[i-1]=findboss(parents[i])
    ans=set(temp)

    print(f'#{tc} {len(ans)}')