name=list(input())

N=int(input())
path=['']*N

def dfs(level):

    if level==N:
        print(*path,sep="")
        return


    for i in range(len(name)):
        path[level] = name[i]
        dfs(level+1)
        path[level] = ''

dfs(0)