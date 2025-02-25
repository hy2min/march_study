n = int(input())

arr = [0, 3, 1, 2, 1, 3, 2, 1, 2, 1, 0]
path = []


def dfs(level):
    if arr[level] == 0:
        path.append('도착')
        return

    path.append(arr[level])
    dfs(level+arr[level])


dfs(n)
path = ['시작'] + path
path.extend(path[:-1][::-1])
print(*path)
