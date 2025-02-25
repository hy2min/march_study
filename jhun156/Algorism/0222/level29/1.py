# import sys
# sys.stdin = open("input.txt","r")

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

path = [0]
used = [0] * N
used[0] = 1

def dfs(num):

    tmp = used.count(1)
    if tmp == N:
        return

    for next in range(N):
        if arr[num][next] == 1 and used[next] == 0:
            used[next] = 1
            path.append(next)
            dfs(next)

dfs(0)
print(*path)