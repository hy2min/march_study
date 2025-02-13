arr = list(map(int, input().split()))
arr2 = []
for i in range(0,6,2) :
    arr2.append(arr[i])

print(arr2)
min_V = min(arr2)
ind  = arr.index(min_V)

print(f"arr[{ind}]={min_V}")