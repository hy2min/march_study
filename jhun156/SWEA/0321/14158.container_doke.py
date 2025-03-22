# import sys
# sys.stdin = open("input.txt","r")

def dfs(level,start):

    global ans
    if level > ans:
        ans = level

    for i in range(N):
        if used[i] == 0 and time_table[i][0] >= start:
            used[i] = 1
            dfs(level+1,time_table[i][1])
            used[i] = 0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    time_table = [list(map(int,input().split())) for _ in range(N)]
    used = [0] * N
    ans = 0

    dfs(0,0)
    print(f"#{tc} {ans}")