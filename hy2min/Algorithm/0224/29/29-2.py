arr = [
    [0,0,1,0,1,1],
    [1,0,0,1,0,0],
    [0,0,0,0,1,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [0,0,0,0,0,0],
]
a, b = map(int, input().split())
a -= 1
b -= 1

visited = [0] * 6
min_route = 21e8

def dfs(level, cnt):
    global min_route
    if level == b:
        min_route = min(min_route, cnt)
        return
    
    for i in range(6):
        if arr[level][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i, cnt + 1)
            visited[i] = 0

visited[a] = 1
dfs(a, 0)
print(min_route if min_route != 21e8 else 0)
