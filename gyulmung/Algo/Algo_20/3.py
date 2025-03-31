lst = list(map(int, input().split()))

def bbq(level):
    print(lst[level], end = " ")

    if len(lst) - 1 == level:
        return

    bbq(level + 1)
    print(lst[level], end = " ")



bbq(0)