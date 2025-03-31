# 자리의 합
import sys

input = sys.stdin.readline

n = input()

l = len(n)


def dfs(x, mul):
    if x == l:
        print(mul)

        return

    dfs(x + 1, mul + int(n[x]))


dfs(0, 0)