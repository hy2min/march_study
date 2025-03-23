n = int(input())
arr = [[] for _ in range(4)]
for _ in range(n):
    a, b = input().split()
    a, b = ord(a) - 65, ord(b) - 65
    arr[a].append(b)
    arr[b].append(a)

visited = [0]*4
flag = 0

def dfs(v, parent):
    visited[v] = 1
    for nv in arr[v]:
        if not visited[nv]:
            if dfs(nv, v):
                return 1
        elif nv != parent:
            return 1
    return 0

for i in range(4):
    if not visited[i]:
        if dfs(i, -1):
            flag = 1
            break

if flag:
    print('발견')
else:
    print('미발견')