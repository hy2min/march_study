# 등수 찾기
import sys
sys.setrecursionlimit(11**5)
input = sys.stdin.readline

N, M, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
arr2 = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr2[b].append(a)

low, high = N, 1

def dfs(x, flag):
    global low, high

    if flag == 0:
        for nxt in arr[x]:
            if visited[nxt] == 1: continue
            low -= 1
            visited[nxt] = 1
            dfs(nxt, flag)

    elif flag == 1:
        for nxt in arr2[x]:
            if visited[nxt] == 1: continue
            high += 1
            visited[nxt] = 1
            dfs(nxt, flag)


for i in range(2):
    visited = [0]*(N+1)
    visited[X] = 1
    dfs(X, i)

print(high)
print(low)
