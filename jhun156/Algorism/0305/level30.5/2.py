OX = 'ox'
n = int(input())
path = [0]*n

def dfs(level):

    if level == n:
        for i in range(n):
            print(path[i],end='')
        print()
        return

    for i in range(2):
        path[level] = OX[i]
        dfs(level+1)

dfs(0)
