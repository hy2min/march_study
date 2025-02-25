arr = list(map(int, input().split()))
used = [0]*5
path = []
Max = -21e8
Min = 21e8
def dfs(x):
    global Max, Min
    if x == 5:
        ret = path[0]*path[1]-path[2]*path[3]+path[4]
        Max = max(Max, ret)
        Min = min(Min, ret)
        return

    for i in range(5):
        if not used[i]:
            used[i] = 1
            path.append(arr[i])
            dfs(x+1)
            used[i] = 0
            path.pop()

dfs(0)
print(Max)
print(Min)
