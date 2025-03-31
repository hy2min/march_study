# import sys
# sys.stdin = open("input.txt","r")

def dfs(level):

    global cnt
    if level == N:
        cnt += 1
        return

    for i in range(N):
        if visited1[i] == visited2[i+level] == visited3[i-level+N] == 0:
            visited1[i] = visited2[i + level] = visited3[i - level + N] = 1
            dfs(level+1)
            visited1[i] = visited2[i + level] = visited3[i - level + N] = 0

T = int(input())
for tc in range(1,T+1):
    cnt = 0
    N = int(input())
    chess = [[0] * N for _ in range(N)]
    visited1 = [0] * N
    visited2 = [0] * (2*N)
    visited3 = [0] * (2*N)
    dfs(0)
    print(f"#{tc} {cnt}")