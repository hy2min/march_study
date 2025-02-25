arr = list(map(int, input().split()))
for i in range(5):
    arr[i+1] = arr[i] + arr[i+1]

print(" ".join(map(str,arr)))