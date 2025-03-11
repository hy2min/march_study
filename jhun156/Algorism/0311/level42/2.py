arr = list(map(int,input().split()))
Max = -21e8
Min = 21e8
path = [0] * 5
used = [0] * 5

def dfs(level):

    global Min,Max
    if level == 5:
        value = path[0]*path[1] - path[2] * path[3] + path[4]
        Max = max(value,Max)
        Min = min(value,Min)

    for i in range(5):
        if used[i] == 0:
            used[i] = 1
            path[level] = arr[i]
            dfs(level+1)
            used[i] = 0

dfs(0)
print(Max)
print(Min)