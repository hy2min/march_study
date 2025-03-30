N,M=map(int,input().split())
schools=list(input().split())
schools.insert(0,0)

arr=[list(map(int,input().split())) for _ in range(M)]
arr.sort(key = lambda x:x[2])
parents=list(range(N+1))
Sum=0
cnt=0
def find_boss(member):

    if parents[member] != member:
        parents[member] = find_boss(parents[member])

    return parents[member]

def union(a,b,c):
    global Sum,cnt
    bossA,bossB=find_boss(a),find_boss(b)

    if bossA==bossB:return
    if schools[a]==schools[b]:return

    Sum+=c
    cnt+=1
    parents[bossB] = bossA

for i in range(M):
    union(arr[i][0],arr[i][1],arr[i][2])


if cnt==N-1:
    print(Sum)
else:
    print(-1)