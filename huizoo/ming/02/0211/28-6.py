st = input()
tree = [list(map(int, input().split())) for _ in range(8)]

visited = [False] * 8

def dfs(n):
    print(st[n], end = '')
    visited[n] = True

    for i in range(8):
        if tree[n][i] == 1 and not visited[i]:
            dfs(i)

dfs(0)