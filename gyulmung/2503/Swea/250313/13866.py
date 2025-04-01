import sys
sys.stdin = open('input.txt','r')

def dfs(lev, Sum):
    global Min, visited
    # 재귀마다 Min값확인
    if Min < Sum: # Sum이 Min보다 크면 리턴
        return

    # 최종합
    if lev == N:
        Min = min(Min, Sum)
        return

    for i in range(N):
        if visited[i] != 1:
            visited[i] = 1
            dfs(lev+1, Sum+arr[lev][i])
            visited[i] = 0
T = int(input())

for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 1e8
    visited = [0]*N
    dfs(0, 0)
    ans = Min

    print(f'#{test} {ans}')