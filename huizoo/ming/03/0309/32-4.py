arr = []
for _ in range(5):
    arr.append(list(input()))
a, b = map(int, input().split())
arr[a].sort()
arr[b].sort()
for row in arr:
    print(row[0], end=' ')