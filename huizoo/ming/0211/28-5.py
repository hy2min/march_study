n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]

path = [0]

def dfs(x, level, max_level):
    if level == max_level:
        print(' '.join(map(str, path)))
        return
    for i in range(n):
        if tree[x][i] == 1 and i not in path:
            path.append(i)
            dfs(i, level+1, max_level)
            path.pop()

dfs(0, 0, 2)