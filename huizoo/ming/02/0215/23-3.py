def dfs(a):
    global cnt
    if a >= 3:
        st = ''.join(path)
        if 'AAA' in st or 'BBB' in st or 'CCC' in st:
            return
    if a == n:
        cnt+=1
        return
    for i in 'ABC':
        path.append(i)
        dfs(a+1)
        path.pop()

n = int(input())
path = []
cnt = 0
dfs(0)
print(cnt)