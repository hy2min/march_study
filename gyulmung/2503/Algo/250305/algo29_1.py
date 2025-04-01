import sys
sys.stdin = open('input.txt','r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(level):
    print(level, end = ' ')

    for i in range(N):
        if arr[level][i] == 1:
            dfs(i)

dfs(0)