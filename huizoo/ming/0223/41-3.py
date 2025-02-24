n, k = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
Min = 21e8
visited = dict()
def abc(x, cnt):
    global Min
    if x > n:
        return
    if cnt >= Min:
        return
    if x == n:
        Min = cnt
        return
    if (x, cnt) in visited and visited[(x, cnt)] <= cnt:
        return
    visited[(x, cnt)] = cnt
    for coin in coins:
        abc(x + coin, cnt + 1)

abc(0, 0)
if Min != 21e8:
    print(Min)
else:
    print('impossible')