import sys
sys.stdin=open('input.txt','r')

import copy
N, M = map(int, input().split())
arr = list(map(int, input().split()))

def bfs(lev, Sum):
    global Min, lst
    if lev == M:
        if Sum < Min:
            Min = Sum
            lst = copy.deepcopy(path)
            return
        return

    for i in range(N):
        if visited[i] != 1:
            path.append(arr[i])
            visited[i] = 1
            bfs(lev+1, Sum * arr[i])
            path.pop()
            visited[i] = 0

Min = 1e8
visited = [0]*N
lst = []
path = []
bfs(0, 1)
print(*sorted(lst))