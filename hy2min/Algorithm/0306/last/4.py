def dfs(level, num):
    global min_n
    if level == 3:
        if int(num) >= 100:
            min_n = min(int(num), min_n)
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(level + 1, num + str(arr[i]))
            visited[i] = 0
n = int(input())
arr = list(map(int, input().split()))
visited = [0] * n
min_n = 21e8

visited[0] = 1
dfs(0,'')

print(min_n)