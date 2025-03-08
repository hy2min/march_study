input_arr = [list(map(int, input().split())) for _ in range(4)]

vect = [[0]*3 for _ in range(4)]

for y, x in input_arr : 
    vect[y][x] = 5

print('\n'.join(' '.join(map(str, row)) for row in vect))