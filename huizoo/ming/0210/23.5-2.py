assasin = [[0]*4 for _ in range(3)]
for _ in range(3) : 
    i, j = map(int, input().split())
    assasin[i][j] = '#'

safe = 1
for row in assasin :
    if row.count('#') == 2 : 
        safe = 0
if safe == 1 : 
    for row in list(zip(*assasin)) : 
        if row.count('#') == 2 : 
            safe = 0

if safe : 
    print('안전')
else : 
    print('위험')
