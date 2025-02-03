arr = [0] * 6
a, b = map(int, input().split())
arr[0] = a
arr[1] = b
for i in range(0, 4):
    arr[i+2] = arr[i] * arr[i+1]

print(arr[-1])