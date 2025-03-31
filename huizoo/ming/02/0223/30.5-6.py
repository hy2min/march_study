n = int(input())
arr = [list(input()) for _ in range(n)]
alp = [chr(i) for i in range(65, 91)]
path = []
cnt = 0
def dfs(x):
    global cnt
    if x == 4:
        cnt += 1
        if path in arr:
            print(cnt)
        return
    for i in alp:
        path.append(i)
        dfs(x+1)
        path.pop()

dfs(0)