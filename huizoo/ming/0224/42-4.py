n = int(input())
coins = [60, 40, 10]
Min = 500
def dfs(x, cnt):
    global Min
    if cnt > Min:
        return
    if x > n:
        return
    if x == n:
        Min = cnt
        return
    for coin in coins:
        dfs(x+coin, cnt+1)

dfs(0, 0)
print(Min)