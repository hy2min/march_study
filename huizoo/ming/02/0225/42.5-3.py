N = int(input())
nums = list(map(int, input().split()))
cnt = 0

def abc(a, b):
    return (a-b)*(a+b)

def bbq(a, b):
    return max(a, b)

def kfc(a, b):
    return a**2-b**2

def bhc(a, b):
    return (a+b)**2

def dfs(n, x):
    global cnt
    if n > 100:
        return
    if x == N-1:
        if n == 100:
            cnt += 1
        return
    for i in range(4):
        if i == 0:
            ret = abc(n, nums[x+1])
        elif i == 1:
            ret = bbq(n, nums[x+1])
        elif i == 2:
            ret = kfc(n, nums[x+1])
        else:
            ret = bhc(n, nums[x+1])
        dfs(ret, x+1)

dfs(nums[0], 0)
print(cnt)