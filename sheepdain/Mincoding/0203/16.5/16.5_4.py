arr=list(map(int,input().split()))
for i in range(4):
    arr.append(arr[i]*arr[i+1])
    print(arr)
print(arr[-1])