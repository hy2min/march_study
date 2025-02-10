arr=list(map(int,input().split()))
a=[]
for i in range(0,6,2):
    a.append(arr[i])
MIN=min(a)
for i in range(6):
    if arr[i]==MIN:
        print(f'arr[{i}]={MIN}')