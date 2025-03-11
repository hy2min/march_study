n = int(input())
arr = list(map(int, input().split()))

min_sum = total = sum(arr[:4])
for i in range(n-4):
    total += arr[i+4]
    total -= arr[i]
    min_sum = min(total,min_sum)
print(min_sum)