# 두 로봇
import sys
input = sys.stdin.readline

def dfs(x):
    global cnt
    if not arr[x]:
        return
    for nxt in arr[x]:
        if not visited[nxt]:
            cnt += 1
            visited[nxt] = 1
            dfs(nxt)

# N = 컴퓨터 수, M = 연결된 컴퓨터 쌍 수
N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0
visited = [0]*(N+1)
visited[1] = 1

dfs(1)

print(cnt)