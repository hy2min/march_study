import sys
sys.stdin = open('input.txt', 'r')

def dfs(lev):
    global Min
    Flag = True
    for i in range(1, n):
        if visited[i]==0:
            Flag = False
            break
    if Flag:
        path[lev] = arr[lev][0]
        Min = min(Min, sum(path))
        return

    for i in range(1, n):
        if visited[i] != 1:
            path[lev] = arr[lev][i]
            visited[i] = 1
            dfs(i)
            visited[i] = 0

T = int(input())
for test in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    path = [0]*n
    visited = [0]*n
    Min = 1e8
    dfs(0)
    print(f'#{test} {Min}')
