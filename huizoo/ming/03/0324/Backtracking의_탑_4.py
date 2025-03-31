# 1, 2, 3 합
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
path = []

def dfs(x, now):
    if x == N:
        print(*path)
        return
    if M == 2:
        for i in range(now, 7):
            path.append(i)
            dfs(x+1, i)
            path.pop()
    else:
        for i in range(1, 7):
            if M == 3 and i in path:
                continue
            path.append(i)
            dfs(x+1, 1)
            path.pop()

dfs(0, 1)