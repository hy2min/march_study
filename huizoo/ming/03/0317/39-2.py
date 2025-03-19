# 모든 코인이 서로 배수 관계에 있기 때문에 그리디 가능?
coins = (500, 100, 50, 10)
N = int(input())

cnt = 0
for coin in coins:
    cnt += N // coin
    N %= coin

print(cnt)