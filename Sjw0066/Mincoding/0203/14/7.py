arr=list(map(int,input().split()))

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] < arr[j] :
            arr[i],arr[j] = arr[j],arr[i]

for i in arr:
    print(i,end="")