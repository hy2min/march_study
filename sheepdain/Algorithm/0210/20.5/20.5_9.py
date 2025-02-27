def isSum(a,b):
    Sum=0
    for i in range(y):
        for j in range(x):
            Sum+=arr[a+i][b+j]
    return Sum

arr=[
    [3,5,4,2,5],
    [3,3,3,2,1],
    [3,2,6,7,8],
    [9,1,1,3,2]
]
y,x=map(int,input().split())
MAX=0
for i in range(5-y):
    for j in range(6-x):
        SUM=isSum(i,j)
        if MAX<SUM:
            MAX=SUM
            idxY,idxX=i,j
print(f'({idxY},{idxX})')
