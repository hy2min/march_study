n = int(input())
arr = list(map(int, input().split()))
Map = [0] + arr + [0] * 7
N = n + 7

memo = [None] * (N + 1)

def dfs(i):
    if i >= n:
        return 0
    if memo[i] is not None:
        return memo[i]

    best = -21e8
    for jump in [2, 7]:
        nxt = i + jump
        Sum = Map[nxt] + dfs(nxt)
        best = max(best, Sum)
    memo[i] = best
    return best

print(dfs(0))
