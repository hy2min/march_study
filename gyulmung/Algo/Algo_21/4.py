N = int(input())

def abc(lev):
    print(lev, end = '')

    if lev == N:
        return

    for i in range(2):
        abc(lev + 1)

abc(0)