arr=list(map(int,input().split()))

masking=[1,0,1,0,1,0]
arr2=[0]*6

for i in range(len(masking)):
    if 1==masking[i]:
        arr2[i]=arr[i]

arr_min=21e8
min_index=21e8

for i in range(6):
    if arr2[i]<arr_min and arr2[i] != 0:
        min_index=i
        arr_min=arr2[i]

print(f'arr[{min_index}]={arr_min}')