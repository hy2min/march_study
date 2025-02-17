s = input()
path = [""] * 3
used = [0] * len(s)
def abc(level):

    if level == 3:
        print("".join(path))
        return
    
    for i in range(4):
        if not used[i]:

            path[level] = s[i]
            used[i] = 1

            abc(level + 1)

            used[i] = 0
abc(0)