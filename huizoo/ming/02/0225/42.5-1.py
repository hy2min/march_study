n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
Max = -10e9
def dfs(level):
    global Max
    if level == n:
        Sum_arr = [0]*n
        for j in range(n):
            for i in range(n):
                Sum_arr[j] += arr[i][j]
        score = 1
        for i in Sum_arr:
            score *= i
        Max = max(Max, score)
        return

    arr2 = arr[level][:]
    for i in range(n):
        arr[level] = arr2[i:] + arr2[:i]
        dfs(level+1)
    arr[level][:] = arr2

dfs(0)
print(Max, '점', sep='')




