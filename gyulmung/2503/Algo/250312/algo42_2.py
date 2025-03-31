import sys
sys.stdin=open('input.txt','r')

lst = list(map(int, input().split()))
visited = [0]*5
path = []
Max = -1e8
Min = 1e8

def dfs(lev):
    global Max, Min
    if lev == 5:
        Sum = (path[0]*path[1])-(path[2]*path[3])+path[4]
        Max = max(Max, Sum)
        Min = min(Min, Sum)

    for i in range(5):
        if visited[i] != 1:
            visited[i] = 1
            path.append(lst[i])
            dfs(lev+1)
            path.pop()
            visited[i] = 0

dfs(0)
print(Max)
print(Min)