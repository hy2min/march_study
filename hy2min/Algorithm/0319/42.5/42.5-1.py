n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

mx = -21e8
def dfs(level,i):
    for j in range(n):
        for i in range(n):
            arr[i][j]

    if mx > total:
        return
    for i in range(n):
        dfs(level+1, (i+1)%n)

ans = list(zip(*arr))
total = 1
for i in ans:
    total *= sum(i)

print(total)