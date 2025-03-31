def dfs(idx, sm):
    global cnt
    if 10 <= sm <= 20:
        cnt += 1
    
    for i in range(idx, len(arr)):
        dfs(i+1, sm+arr[i])

arr = list(map(int, input().split()))
cnt = 0
dfs(0,0)

print(cnt)