level = int(input())
branch = int(input())

def abc(lev):
    if lev == level:
        return

    for i in range(branch):
        abc(lev + 1)

abc(0)