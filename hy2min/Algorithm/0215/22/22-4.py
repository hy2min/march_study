def abc(level,floor):
    if level == 5:
        if floor < 1:
            print(f'B{abs(floor-1)}')
        else:
            print(floor)
        return
    
    s = input()

    if s =="up":
        abc(level+1, floor +1)
    elif s == 'down':
        abc(level+1, floor-1)

abc(0,1)