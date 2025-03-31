name=list(map(str,input().split()))
path=[0]*3
visited=[0]*3

def abc(level):

    if level==3:
        print(*path,sep="")

        return

    for i in range(3):
        if visited[i] == 1:continue
        path[level]=name[i]
        visited[i]=1
        abc(level+1)
        visited[i]=0
        path[level]=0

abc(0)