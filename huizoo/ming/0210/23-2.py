alps = input()
path = []
cnt = 0
def dfs(level, max_level):
    global cnt
    if level == max_level:
        cnt += 1
        return
    for alp in alps:
        if path:
            if (
                (path[-1] == 'B' and alp == 'T') or
                (path[-1] == 'T' and alp == 'B')
            ):
                pass
            else:
                path.append(alp)
                dfs(level+1, max_level)
                path.pop()
        else:
            path.append(alp)
            dfs(level+1, max_level)
            path.pop()

dfs(0, 4)
print(cnt)