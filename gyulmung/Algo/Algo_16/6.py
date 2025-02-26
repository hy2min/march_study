arr = list(map(int, input().split()))

for i in range(len(arr)-1):
    arr[i+1] = arr[i] + arr[i+1]
print(*arr)