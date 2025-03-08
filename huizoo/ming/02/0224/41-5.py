cards = list(input().split())
path = []
def dfs(x):
    if x == 3:
        print(*path, sep='')
    for card in cards:
        if card not in path:
            path.append(card)
            dfs(x+1)
            path.pop()
dfs(0)