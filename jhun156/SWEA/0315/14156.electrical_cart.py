# import sys
# sys.stdin = open("input.txt","r")

def dfs(level,Sum,y):       # level = 몇군데를 들렸느지 확인, Sum = 합, y = 현재 몇번째 줄(행)에 있는지
                            # 인자를 3개를 받아야 하는 이유 : 현재 내가 몇번째 줄에 있는지 확인하는데 필요한 정보
    global Min              # 하... 한시간날렸네 아 짜증나ㅏㅏㅏㅏㅏㅏ

    if Sum > Min:
        return

    if level == N - 1:
        Sum += arr[y][0]
        Min = min(Min,Sum)
        return

    for i in range(N):
        if y == i: continue
        if visited[i] == 1: continue
        visited[i] = 1
        dfs(level+1, Sum + arr[y][i],i)
        visited[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1
    Min = 21e8
    dfs(0,0,0)
    print(f"#{tc} {Min}")