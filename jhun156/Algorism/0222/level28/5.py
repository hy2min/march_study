# import sys
# sys.stdin = open("input.txt","r")

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
path = [0]
used = [0] * N
used[0] = 1

def dfs(num,level):

    if level == 2:
        print(*path)
        return

    for next in range(N):
        if arr[num][next] == 1 and used[next] == 0:
            used[num] = 1
            path.append(next)
            dfs(next,level+1)
            path.pop()

dfs(0,0)