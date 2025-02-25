arr = [3,5,1,9,7]
a = [input() for _ in range(4)]

def dfs(arr,level):
    if level == 4:
        return
    if a[level] == 'R':
        arr[:] = [arr[-1]]+arr[:-1]
        dfs(arr, level + 1)
    elif a[level] == 'L':
        arr[:] = arr[1:]+[arr[0]]
        dfs(arr, level + 1)

dfs(arr, 0)
print(*arr)