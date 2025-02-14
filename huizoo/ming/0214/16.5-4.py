a, b = map(int, input().split())
arr = [a, b]
for i in range(2, 6):
    arr.append(arr[i-1]*arr[i-2])

print(arr[-1])