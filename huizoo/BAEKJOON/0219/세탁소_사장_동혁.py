T = int(input())
for _ in range(T):
    C = int(input())
    coin = [25, 10, 5, 1]
    dis = [0, 0, 0, 0]
    i = 0
    while C > 0:
        if C >= coin[i]:
            while C >= coin[i]:
                dis[i] += (C//coin[i])
                C %= coin[i]
        i += 1
    print(*dis)
