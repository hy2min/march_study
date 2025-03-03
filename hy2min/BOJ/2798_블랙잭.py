n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = -21e8

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            if arr[i] + arr[j] + arr[k] <= m and arr[i] + arr[j]+arr[k] > max_sum:
                max_sum = arr[i]+arr[j]+arr[k]

print(max_sum)
