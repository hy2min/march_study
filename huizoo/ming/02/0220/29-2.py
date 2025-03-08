def dfs(x, Sum):
    global Min, flag
    if x == B:
        flag = 1
        Min = min(Min, Sum)
        return
    for i in arr[x]:
        if i not in path:
            path.append(i)
            dfs(i, Sum+1)

A, B = map(int, input().split())
arr = [
    [],
    [3,5,6],
    [1,4],
    [5],
    [1],
    [1],
    [],
]
path = [A]
Min = 21e8
flag = 0
dfs(A, 0)
if flag:
    print(Min)
else:
    print(0)