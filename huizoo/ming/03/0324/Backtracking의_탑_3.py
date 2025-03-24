# 1, 2, 3 합
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
def dfs(x):
    global cnt
    if x == N:
        cnt += 1
        return

    for nxt in (x+1, x+2, x+3):
        if nxt <= N:
            dfs(nxt)
dfs(0)
print(cnt)