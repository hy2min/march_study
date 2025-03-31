
def dfs(level, tri):
    print(*tri)
    if level == N-1:
        return
    if len(tri) == 1:
        tri.append(1)
    else:
        for i in range(len(tri)-1):
            tri.insert(i+1, tri[2*i]+tri[2*i+1])
        if level >= 2:
            for i in range(level-1):
                tri.pop(len(tri)-2)
    dfs(level+1, tri)

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [1]
    print(f'#{tc}')
    dfs(0, arr)