def dfs(level, Sum):
    if level >= n+1:
        max_sum = max(max_sum,Sum)
        return
    for i in [2,7]:
        if level+i < n+1:
            dfs(level+i, Sum+arr[level+i])

n = int(input())
arr = [0]+list(map(int,input().split()))+[0]
max_sum = -21e8
dfs(0,0)
print(max_sum)