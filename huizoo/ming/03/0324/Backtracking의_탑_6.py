# N Queen
import sys
input = sys.stdin.readline

N = int(input())
col = [0]*N
dia1 = [0]*(2*N)
dia2 = [0]*(2*N)
cnt = 0
def dfs(x):
    global cnt
    if x == N:
        cnt += 1
        return
    for i in range(N):
        if col[i] == 0 and dia1[i+x] == 0 and dia2[i-x+N] == 0:
            col[i] = 1
            dia1[i+x] = 1
            dia2[i-x+N] = 1
            dfs(x+1)
            col[i] = 0
            dia1[i+x] = 0
            dia2[i-x+N] = 0
dfs(0)
print(cnt)