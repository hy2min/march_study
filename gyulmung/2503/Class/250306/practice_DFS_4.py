from copy import deepcopy

arr = [[3, 1, 9, 6],
       [6, 5, 9, 6],
       [5, 8, 4, 7],]

diry = [0, 0, 1, -1]
dirx = [1, -1, 0, 0]
Max = -1e8
Sum = 0
def dfs(now):
    global Max, Sum
    if now == 4:
        Sum = 0
        for i in range(3):
            Sum += sum(arr[i])
        Max = max(Max, Sum)
        return
    dig = []
    dig = deepcopy(arr)
    for i in range(3):
        for j in range(4):
            for k in range(4):
                dy = diry[k] + i
                dx = dirx[k] + j
                if dy < 0 or dx < 0 or dy > 2 or dx > 3:
                    continue
                arr[i][j] = (arr[i][j]*7)%10
                arr[dy][dx] = (arr[dy][dx]*7)%10
                dfs(now + 1)

dfs(0)
print(Max)