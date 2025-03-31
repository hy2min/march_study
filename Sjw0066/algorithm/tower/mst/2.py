N,K = map(int,input().split())
bat=[list(map(int,input().split())) for _ in range(N)]
parent=list(range(N))
arr=[]
Sum=0
cnt=0

for i in range(N):
    for j in range(i+1,N):
        cost=(bat[i][0]-bat[j][0])**2 + (bat[i][1]-bat[j][1])**2
        if cost>=K:
            arr.append((cost,i,j))
arr.sort()
def find_boss(member):

    if parent[member] != member:
        parent[member] = find_boss(parent[member])
    return parent[member]

def union(a,b,c):
    global Sum,cnt
    bossA,bossB=find_boss(a),find_boss(b)

    if bossA==bossB:
        return

    Sum+=c
    cnt+=1
    parent[bossB]=bossA


for i in range(len(arr)):
    c,a,b=arr[i][0],arr[i][1],arr[i][2]
    union(a,b,c)
    if cnt==N-1:break


if cnt==N-1:
    print(Sum)
else:
    print(-1)







