arr=list(map(int,input().split()))
cnt=0

def dfs(level,Sum):
    global cnt

    if level==len(arr):
        return

    if 10 <= Sum + arr[level] <= 20:
        cnt+=1

    for i in range(2):
        dfs(level+1,Sum+arr[level]*i)


dfs(0,0)
print(cnt)