n = int(input())
arr = []
for _ in range(n):
    arr.append(input().split())
arr.sort(key=lambda x: (x[0], x[1]))
for row in arr:
    print(*row)