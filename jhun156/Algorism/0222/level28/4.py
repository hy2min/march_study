# N*N 으로 인접행렬을 입력받고, DFS 탐색 순서 출력
# import sys
# sys.stdin = open("input.txt","r")

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

used = [0] * N
used[0] = 1
path = [0]

def dfs(num):

    tmp = used.count(1)
    if tmp == N:
        return

    for next_node in range(N):
        if arr[num][next_node] == 1 and used[next_node] == 0:
            used[next_node] = 1
            path.append(next_node)
            dfs(next_node)

dfs(0)
print(*path)