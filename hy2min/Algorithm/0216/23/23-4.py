n = int(input())

member = "BTSKR"
cnt = 0
path = [""] * n
used = [0] * len(member)

def abc(level):
    global cnt

    if level == n:
        if "S" in path:
            cnt += 1
        return
    
    for i in range(5):
        if not used[i]:
            path[level] = member[i]
            used[i] = 1
            abc(level + 1)
            used[i] = 0

abc(0)
print(cnt)