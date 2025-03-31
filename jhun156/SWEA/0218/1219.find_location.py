import sys
sys.stdin = open("input.txt","r")

T = 10
for tc in range(1,T+1):
    T,N = map(int,input().split())
    arr = list(map(int,input().split()))
    connect = [[] for _ in range(N+1)]
    for i in range(0,2*N,2):
        connect[arr[i]].append(arr[i+1])
    visited = [0] * 100

    def dfs(s,g):
        stack = [s]
        visited[s] = 1

        while True:
            now = stack.pop()
            if now == g:
                return 1

            for next in connect[now]:
                if visited[next] == 0:
                    visited[next] = 1
                    stack.append(next)

            if not stack:
                return 0

    ans = dfs(0,99)
    print(f"#{T} {ans}")