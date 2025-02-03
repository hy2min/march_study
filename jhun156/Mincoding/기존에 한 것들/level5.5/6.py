arr = [3,5,1,2,4,6,7]

a,b = map(int,input().split())

for i in arr[a:b+1]:
    print(i,end=' ')