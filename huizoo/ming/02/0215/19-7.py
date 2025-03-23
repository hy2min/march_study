input1 = [list(map(int, input().split())) for _ in range(4)]
vect1 = [[0]*3 for _ in range(4)]
for i in range(4):
    vect1[input1[i][0]][input1[i][1]] = 5

print('\n'.join(' '.join(map(str, row)) for row in vect1))