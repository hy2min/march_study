n = int(input())
arr = input().split()
path = []
visited = [0]*n
Min = 21e8
def dfs(level):
    global Min
    if level == 3:
        val = int(''.join(path))
        if val >= 100:
            Min = min(Min, val)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            path.append(arr[i])
            dfs(level+1)
            visited[i] = 0
            path.pop()

dfs(0)
print(Min)