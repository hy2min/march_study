def dfs(level):
    global cnt
    if level>=2:
        if abs(path[-1]-path[-2]) > 3:
            return
    if level == 4:
        cnt+=1
        return
    for card in cards:
        path.append(card)
        dfs(level+1)
        path.pop()

cards = list(input())
for i in range(5):
    cards[i] = int(cards[i])
path = []
cnt = 0
dfs(0)
print(cnt)