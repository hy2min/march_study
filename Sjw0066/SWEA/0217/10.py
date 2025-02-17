name=[chr(i) for i in range(65,91)]
path=['']*4


def dfs(level,target):
    global cnt

    if level==4:
        cnt += 1
        if path==target:
            print(cnt)
        return


    for i in range(len(name)):
        path[level] = name[i]
        dfs(level+1,target)
        path[level] = ''

n=int(input())

for i in range(n):
    cnt = 0
    pw=list(input())
    dfs(0,pw)
