n = int(input())
santa = 'BTSKR'
path = [0]*n
cnt = 0
used = [0]*5
def abc(lev):
    global path, cnt

    if lev == n:
        for i in path:
            if i == 'S':
                cnt += 1
        return

    for i in range(5):
        if used[i] == 0:
            used[i] = 1
            path[lev] = santa[i]
            abc(lev + 1)
            used[i] = 0
        continue
    return cnt

result = abc(0)
print(result)