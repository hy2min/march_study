n = int(input())
arr = list(map(int, input().split()))
burned = [0]*n
path = []
Max = -100
ans = []
def dfs(Sum):
    global burned, Max, ans
    if 0 not in burned:
        if Max < Sum:
            Max = Sum
            ans = path[:]
        return
    for i in range(n):
        if not burned[i]:
            temp = burned[:]
            for j in range(-1, 2, 1):
                if 0<= i+j < n:
                    burned[i+j] = 1
            path.append(arr[i])
            dfs(Sum+arr[i])
            path.pop()
            burned = temp[:]

dfs(0)
print(*ans, sep='+', end='')
print(f'={Max}')