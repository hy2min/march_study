import sys
sys.stdin = open("input.txt", "r")

def abc(x, now, Sum):
    global Min
    if x == N-1:
        Min = min(Min, Sum+arr[now][0])
        return

    if Sum >= Min:
        return

    for i in range(1, N):
        if visited[i] == 1:continue
        visited[i] = 1
        abc(x+1, i, Sum+arr[now][i])
        visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 1e9
    for i in range(1, N):
        visited = [0]*N
        visited[i] = 1
        abc(1, i, arr[0][i])

    print(f'#{tc} {Min}')