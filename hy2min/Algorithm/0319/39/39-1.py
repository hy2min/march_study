arr = list(map(int, input().split()))
total = sum(arr)
arr.sort()

for i in range(1, len(arr)):
    arr[i] += arr[i-1]

print(sum(arr) - total)