import copy
arr=[list(input()) for _ in range(4)]
N=int(input())
visited=[[0]*4 for _ in range(4)]
path=[0]*N
answer=[]
Min=21e8
direct_y=[1,-1,0,0,0]
direct_x=[0,0,-1,0,1]

def check_servive(arr2):
    cnt=0
    for i in range(4):
        for j in range(4):
            if arr2[i][j] != '_':
                cnt+=1
    return cnt

def bomb(y,x):
    for k in range(5):
        dy=direct_y[k] + y
        dx=direct_x[k] + x
        if dy > 3 or dy < 0 or dx > 3 or dx < 0:continue
        arr[dy][dx] = '_'



def dfs(y,x,level):
    global answer,Min,arr

    if level==N:
        live=check_servive(arr)
        if Min>live:
            Min=live
            answer=path[:]
        return


    temp=copy.deepcopy(arr)

    for i in range(4):
        for j in range(4):
            if arr[i][j] == '_':continue
            if visited[i][j] == 1: continue
            path[level] = arr[i][j]
            bomb(i, j)
            visited[i][j] = 1
            dfs(i,j,level+1)
            visited[i][j] = 0
            arr=copy.deepcopy(temp)

dfs(0,0,0)
answer.sort()
print(*answer)
