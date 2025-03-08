cards = list(input())
for i in range(len(cards)) : 
    cards[i] = int(cards[i])
pick = []
def dfs(level, max_level) : 
    if level == max_level : 
        return 1
    cnt = 0
    for card in cards : 
        if len(pick) < 1 : 
            pick.append(card)
            cnt += dfs(level+1, max_level)
            pick.pop()
        elif abs(pick[-1] - card) <= 3 : 
            pick.append(card)
            cnt += dfs(level+1, max_level)
            pick.pop()
        
    return cnt

print(dfs(0, 4))