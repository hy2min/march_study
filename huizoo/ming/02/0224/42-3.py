st = input()
pos = ['BTS', 'SBS','BS','CBS','SES']
com = []
length = len(st)
Min = 50
def dfs(x):
    global Min
    if x > length:
        return
    if x == length:
        if st == ''.join(com):
            Min = min(Min, len(com))
        return
    for po in pos:
        com.append(po)
        dfs(x+len(po))
        com.pop()

dfs(0)
print(Min)