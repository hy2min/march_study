arr=list(map(int,input().split()))
a=[]
for i in range(0,6,2):
    a.append(arr[i])
MIN=min(a)
for i in range(3):
    if a[i]==MIN:
        print(f'arr[{i}]={MIN}')