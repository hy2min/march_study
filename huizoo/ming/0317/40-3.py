arr = list(map(int, input().split())) + [0]*2
arr[1] = -21e8

for i in range(3, 14):
    arr[i] = arr[i] + max(arr[i-2], arr[i-3])

print(max(arr[11:]))
