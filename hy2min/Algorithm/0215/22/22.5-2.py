n = int(input())

def date(level,ox):

    if level == n:
        print(ox, end="")
        print()
        return
    for i in ['x','o']:
        date(level+1, ox + i)

date(0,'')
