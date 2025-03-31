n = int(input())
hero = ['B','I','A','H']
pick = 0
while len(hero) > 1:
    pick = (pick + n-1)%len(hero)
    print(hero.pop(pick), end=' ')
print(hero[0])