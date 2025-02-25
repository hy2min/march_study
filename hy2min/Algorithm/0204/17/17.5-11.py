arr = [3, 5, 4, 2]
masking = list(map(int, input().split()))
total = 0
for i in range(len(arr)):
    if masking[i] == 1:
        total += arr[i]
print(total)