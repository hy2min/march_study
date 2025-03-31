def abc(level):
    print('@', end=' ')
    if level==2:
        return

    print('@', end=' ')
    for i in range(2):
        abc(level+1)
        print('@', end=' ')

abc(0)