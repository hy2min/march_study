def bbq(level):

    level += 1
    if level == 10:
        return 0
    bbq(level)

bbq(0)