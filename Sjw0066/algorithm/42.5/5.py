food = list(map(int, input().split()))
turn = int(input())
Max = -21e8


def dfs(level, lst, Sum):
    global Max

    if level % 3 == 0:
        if level != 0:
            for i in range(6):
                lst[i] *= 2

    if level == turn * 3:
        if Max < Sum:
            Max = Sum
        return

    temp = lst[:]

    if level % 3 == 0:
        for i in range(3):
            ret = lst[i]
            lst[i] = 0
            dfs(level + 1, lst, Sum + ret)
            lst = temp[:]
    elif level % 3 == 1:
        for i in range(3, 6):
            ret = lst[i]
            lst[i] = 0
            dfs(level + 1, lst, Sum + ret)
            lst = temp[:]
    elif level % 3 == 2:
        for i in range(1, 5):
            ret = lst[i]
            lst[i] = 0
            dfs(level + 1, lst, Sum + ret)
            lst = temp[:]


dfs(0, food, 0)
print(Max)
