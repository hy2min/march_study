# import sys
# sys.stdin = open("input.txt","r")

def dfs(level):
    global ans
    if level == N:
        ans += 1
        return

    for i in range(N):
        if used_flat[i] == 1:
            continue
        if used_up[level+i] == 1:
            continue
        if used_down[N-level+i] == 1:
            continue
        used_flat[i],used_up[level+i],used_down[N-level+i] = 1,1,1
        dfs(level+1)
        used_flat[i], used_up[level + i], used_down[N - level + i] = 0,0,0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    used_flat = [0]*N
    used_up = [0]*(2*N)
    used_down = [0]*(2*N)
    ans = 0

    dfs(0)
    print(f"#{tc} {ans}")