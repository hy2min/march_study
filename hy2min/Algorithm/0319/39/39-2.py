def dfs(n, cnt):
    global min_cnt

    if n < 0 or cnt > min_cnt:
        return

    if n == 0:
        min_cnt = min(min_cnt, cnt)
        return

    for coin in coins:
        dfs(n-coin, cnt+1)

total = int(input())

coins = [500,100,50,10]
min_cnt = 21e8

dfs(total, 0)

print(min_cnt)