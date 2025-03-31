import sys
input = sys.stdin.readline

N = int(input())
arr = ('1', '2', '3')
def dfs(x, path):
    for i in range(1, x//2+1):
        if path[x-i:] == path[x-2*i:x-i]:
            return

    if x == N:
        print(int(path))
        exit()

    for i in arr:
        dfs(x+1, path+i)

dfs(0, '')