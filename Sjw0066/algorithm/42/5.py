N=int(input())
target=10
cnt=0
def dfs(level,Sum):
    global cnt

    if Sum>10:
        return

    if level == N:
        if Sum == 10:
            cnt+=1
        return

    for i in range(1,10):
        dfs(level+1,Sum+i)

dfs(0,0)
print(cnt)