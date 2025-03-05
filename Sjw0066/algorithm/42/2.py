lst=list(map(int,input().split()))
path=[0]*5
used=[0]*5

Min=21e8
Max=-21e8

def cal(lst):
    ret=lst[0]*lst[1] - lst[2]*lst[3] + lst[4]
    return ret


def dfs(level):


    for i in range(5):
        if used[i] == 1 : continue
        path[level]=lst[i]
        used[i] = 1
        dfs(level+1)