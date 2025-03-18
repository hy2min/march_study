import sys
sys.stdin = open("input.txt", "r")

def abc(level, multi):
    global Max
    if multi <= Max:
        return
    if level == N:
        Max = max(Max, multi)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            abc(level + 1, multi * arr[level][i] / 100)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Max = 0
    visited = [0]*N
    abc(0, 1)
    print(f'#{tc} {Max*100:6f}')