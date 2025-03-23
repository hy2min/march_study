n = int(input())
arr = list(map(int, input().split()))
Min = 0
now = 0
for i in range(4):
    Min += arr[i]
    now = Min
for i in range(4, n):
    now = now - arr[i-4] + arr[i]
    Min = min(Min, now)
print(Min)