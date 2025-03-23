n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    idx, name = input().split()
    arr[int(idx)].append(name)
print(*max(arr, key=len))