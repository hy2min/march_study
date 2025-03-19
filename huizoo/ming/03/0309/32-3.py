n = int(input())
arr = list(map(int, input().split()))
for i in range(n-3, -1, -1):
    if len(set(arr[i:i+3])) == 1:
        for _ in range(3):
            arr.pop(i)
arr.sort()
print(*arr)