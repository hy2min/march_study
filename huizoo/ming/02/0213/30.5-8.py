n = int(input())
hero = ['B','I','A','H']
i = 0
m = 0
for i in range(4):
    m = (m + n) % len(hero) - 1
    print(hero.pop(m), end=' ')



