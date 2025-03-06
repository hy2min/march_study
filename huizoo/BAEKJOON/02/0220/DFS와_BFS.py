N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(1, N+1):
    arr[i].sort()

def dfs(x):
    print(x, end=' ')
    for i in arr[x]:
        if i not in path1:
            path1.append(i)
            dfs(i)

def bfs(x):
    q = []
    q.append(x)
    while q:
        now = q.pop(0)
        print(now, end=' ')
        for i in arr[now]:
            if i not in path2:
                path2.append(i)
                q.append(i)

path1 = [V]
dfs(V)
print()
path2 = [V]
bfs(V)