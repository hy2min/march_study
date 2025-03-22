# 사회망 서비스(SNS)
import sys
input = sys.stdin.readline


N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(node, parent, is_early_adopter):
    cnt = 1 if is_early_adopter else 0

    for child in arr[node]:
        if child != parent:
            if is_early_adopter:
                cnt += min(dfs(child, node, True), dfs(child, node, False))
            else:
                cnt += dfs(child, node, True)

    return cnt

print(min(dfs(1, 0, True), dfs(1, 0, False)))