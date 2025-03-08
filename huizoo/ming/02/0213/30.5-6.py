def dfs(level):
    global cnt
    if level == 4:
        cnt += 1
        if path == st:
            print(cnt)
        return
    for char in alp:
        path.append(char)
        dfs(level+1)
        path.pop()


path = []
alp = [chr(i) for i in range(65, 91)]
n = int(input())
for _ in range(n):
    cnt = 0
    st = list(input())
    dfs(0)

