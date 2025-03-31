arr = [[0, 0, 1, 0, 1, 1],
       [1, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 1, 0],
       [1, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]
visited = [0]*6
y, x = map(int, input().split())
y -= 1
x -= 1
cnt = 0
ret = 0
def dfs(now):
    global cnt, ret
    if now == x:
        ret = cnt
        return

    for i in range(6):
        if arr[now][i] == 1 and visited[i] == 0:
            visited[i] = 1
            cnt+=1
            dfs(i)
            cnt-=1

dfs(y)
if ret > 0:
    print(ret)
else:
    print(0)