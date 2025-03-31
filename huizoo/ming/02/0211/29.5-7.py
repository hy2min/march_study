worm, life = map(int, input().split())

ground = ['_']*5

for i in range(life+1):
    if i == 0:
        ground[worm] = life
    elif life == 0:
        ground[worm+i-1] = '_'
    else:
        ground[worm+i-1], ground[worm+i] = '_', life
    
    print(''.join(map(str, ground)))
    life -= 1
    
         