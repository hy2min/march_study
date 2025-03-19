n = int(input())
cost = [1, 2, 3, 3, 5, 1, 0, 1, 3]
Min = 0
now = 0
for i in range(n):
    Min += cost[i]
    now = Min
for i in range(n, 9):
    now = now - cost[i-n] + cost[i]
    Min = min(Min, now)
print(Min)