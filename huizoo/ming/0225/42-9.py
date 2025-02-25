n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
Max = -10e9
used = [[0]*n for _ in range(n)]
path = []
def dfs(x):
    if x == n:
        return
    Sum = 0
    for j in range(n):
        for i in range(n):
            Sum += arr[i][j]

dfs(0)