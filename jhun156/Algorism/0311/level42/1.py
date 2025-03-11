string = input()
n = len(string)
path = [0] * 3

def dfs(start,level):

    if level == 3:
        print("".join(path))
        return

    for i in range(start,n):
        path[level] = string[i]
        dfs(i,level+1)

dfs(0,0)