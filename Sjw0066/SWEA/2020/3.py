arr=[list(map(int,input().split())) for _ in range(6)]

name=['A','B','C','D','E','F']
path=[0]*6

def dfs(now):

    if  1 not in arr[now]:
        for i in path:
            if i :
                print(i,end="")
        print()
        return


    for i in range(6):
        if arr[now][i] != 1: continue
        path[now+1]=name[i]
        dfs(i)
        path[now+1] = 0

path[0] = name[0]
dfs(0)