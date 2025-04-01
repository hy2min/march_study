string = list(map(str, input()))


def bbq(level):
    print(string[level], end = '')

    if level == 4:
        print()
        print(string[level], end = '')
        return
    
    bbq(level + 1)
    print(string[level], end = '')


bbq(0)