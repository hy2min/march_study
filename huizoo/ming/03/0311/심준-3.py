arr = [list(map(int, input().split())) for _ in range(6)]
lst = [chr(i) for i in range(65, 71)]
path = ['A']
def dfs(x):
    if 1 not in arr[x]:
        print(''.join(path))
        return
    for i in range(6):
        if arr[x][i] and lst[i] not in path:
            path.append(lst[i])
            dfs(i)
            path.pop()

dfs(0)
