from collections import Counter

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
bit = [list(map(int, input().split())) for _ in range(n)]

lst = []
for i in range(n):
    for j in range(n):
        if bit[i][j] == 1:
            lst.append(arr[i][j])

count = Counter(lst)
lst.sort(key=lambda x:(-count[x], x))
print(*lst)