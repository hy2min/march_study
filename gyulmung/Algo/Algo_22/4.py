stairs = [input() for _ in range(5)]

where = 0

def layer(lev):
    global where

    if lev == 5:
        return

    if stairs[lev] == 'up':
        where += 1
    elif stairs[lev] == 'down':
        where -= 1

    layer(lev + 1)


layer(0)
if where < 0:
    print(f'B{abs(where)}')
else:
    print(where+1)
