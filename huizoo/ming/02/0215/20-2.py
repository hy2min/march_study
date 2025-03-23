n = int(input())
def rec(level):
    print(level, end = ' ')
    if level == 0:
        return
    rec(level-1)
    print(level, end = ' ')
rec(n)