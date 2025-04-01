import sys
sys.stdin=open('input.txt','r')

arr = list(input().split())
path= [0]*len(arr)
visited = [0]*len(arr)
def dfs(level):
    if level == len(arr):
        print(*path, sep = "")
        return

    for i in range(len(arr)):
        if visited[i] != 1:
            visited[i] = 1
            path[level] = arr[i]
            dfs(level+1)
            visited[i] = 0

dfs(0)