n = int(input())
nums = [i for i in range(1, 10)]
cnt = 0
def dfs(x, Sum):
    global cnt
    if Sum > 10:
        return
    if x == n:
        if Sum == 10:
            cnt += 1
    for num in nums:
        dfs(x+1, Sum+num)

dfs(0, 0)
print(cnt)