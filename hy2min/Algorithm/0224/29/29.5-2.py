n = int(input())
evid = [-1, 0, 0, 1, 2, 4, 4]
timestamp = [8, 3, 5, 6, 8, 9, 10]
path = []


def dfs(n):
    if evid[n] == -1:
        path.append(n)
        return

    path.append(n)
    dfs(evid[n])


dfs(n)
path = path[::-1]
for i in path:
    if evid[i] == -1:
        time = '출발'
    else:
        time = str(timestamp[i]) + '시'
    print(f'{i}번index({time})')
