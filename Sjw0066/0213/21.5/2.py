arr=[
    [3,4,1,5],
    [3,4,1,3],
    [5,2,3,6],
]

Sum=[]
col_sum=0

for i in range(4):
    col_sum=0
    for j in range(3):
        col_sum+=arr[j][i]
    Sum.append(col_sum)

index=int(input())
print(Sum[index])
