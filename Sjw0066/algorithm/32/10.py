N=int(input())

arr=[list(map(int,input().split())) for _ in range(N)]
bit=[list(map(int,input().split())) for _ in range(N)]
ans=[]
for i in range(N):
    for j in range(N):
        if bit[i][j]:
            ans.append(arr[i][j])

ret=sorted(ans,key=lambda x:(-ans.count(x),x))

print(*ret )