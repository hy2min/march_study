tree = [1, 2, 3, 4, 5, 6]
tree_arr = [
    [0, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

visited = [False] * 6

level = 0
flag = 0
def dfs(a, b):
    global level, flag
    if a == b : 
        print(level)
        flag = 1
        return
    visited[a] = True
    for i in range(6):
        if tree_arr[a][i] == 1 and not visited[i]:
            level += 1
            dfs(i, b)
            level -= 1

A, B = map(int, input().split())

dfs(tree.index(A), tree.index(B))
if not flag:
    print(0)