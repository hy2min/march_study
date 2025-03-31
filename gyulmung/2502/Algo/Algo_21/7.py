string = input()
N = len(string)

def abc(lev):
    print(lev, end=' ')
    if lev == 1:
        return

    abc(lev - 1)
    print(lev, end = ' ')

abc(N)