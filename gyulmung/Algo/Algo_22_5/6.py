strings = [input() for _ in range(4)]
path = []
Min = 1e8


def abc(lev):
    global Min
    if lev == len(strings):
        path.append(strings.pop(Min_w))
        return
    for i in range(len(strings)):
        if Min > len(strings[lev]):
            Min = len(strings[lev])
            Min_w = lev
            abc(lev + 1)






abc(0)