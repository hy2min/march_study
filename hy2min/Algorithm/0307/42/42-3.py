def dfs(cnt, path):
    global mn
    if path not in char:
        return
    if path == char:
        mn = min(cnt, mn)
        return
    for i in range(5):
        dfs(cnt+1, path+arr[i])
arr = ['BTS', 'SBS', 'BS', 'CBS', 'SES']
mn = 21e8
char = input()
dfs(0,'')
print(mn)