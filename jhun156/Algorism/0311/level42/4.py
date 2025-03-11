price = int(input())
coins = [10,40,60]
Min = 1000

def dfs(level,Sum):
    global Min
    if Sum < 0 or level > Min:
        return

    if Sum == 0:
        Min = min(Min,level)

    for i in range(3):
        dfs(level+1,Sum-coins[i])

dfs(0,price)
print(Min)