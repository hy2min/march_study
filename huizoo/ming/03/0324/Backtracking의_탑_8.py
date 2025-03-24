# 다빈치 타워
import sys, copy
input = sys.stdin.readline

N, M = map(int, input().split())
tower = [list(map(int, input().split())) for _ in range(N)]

Max = -21e8
def dfs(x, lst):
    global Max
    if x == N:
        value = 1
        for j in range(M):
            Sum = []
            for i in range(N):
                if lst[i][j] not in Sum:
                    Sum.append(lst[i][j])
                else:
                    return
            value *= sum(Sum)
        Max = max(Max, value)
        return

    for i in range(M):
        lst2 = copy.deepcopy(lst)
        lst2[x] = lst[x][i:] + lst[x][:i]
        dfs(x+1, lst2)


dfs(0, tower)
print(Max)