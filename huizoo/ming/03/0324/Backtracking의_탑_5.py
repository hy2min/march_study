# N Castle
import sys
input = sys.stdin.readline

N = int(input())
hor = [0]*N
cnt = 0
def dfs(x):
    global cnt
    if x == N:
        cnt += 1
        return
    for i in range(N):
        if hor[i] == 0:
            hor[i] = 1
            dfs(x+1)
            hor[i] = 0
dfs(0)
print(cnt)