import math
N=int(input())
arr=[
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
lst=[]

for _ in range(N):
    a,b,c=map(int,input().split())
    arr[a][b]= c
    lst.append((a,b))

M=int(input())
lst=list(map(int,input().split()))
for wind in lst:
    for i in range(3):
        for j in range(3):
            if arr[i][j] % 10 >wind:
                arr[i][j]-=wind
            else:
                arr[i][j] //=10

cnt=0
for i in range(3):
    for j in range(3):
        if arr[i][j]:
            cnt+=math.ceil(math.log10(arr[i][j]))

print(cnt)


