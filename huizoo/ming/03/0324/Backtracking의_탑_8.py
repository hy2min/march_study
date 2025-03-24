# 다빈치 타워
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tower = [list(map(int, input().split())) for _ in range(N)]
Max = -1e9

def dfs(x, rotate):
    global Max
    if x == N:
        mul = 1
        for j in range(M):
            seen = set()
            for i in range(N):
                val = tower[i][(j + rotate[i]) % M]
                if val in seen:
                    return
                seen.add(val)
            mul *= sum(seen)
        Max = max(Max, mul)
        return

    for i in range(M):
        rotate[x] = i
        dfs(x+1, rotate)


dfs(0, [0]*N)
print(Max)