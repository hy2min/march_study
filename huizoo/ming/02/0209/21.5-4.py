spaceship = [list(input()) for _ in range(4)]

for i in range(3, -1, -1) : 
    for j in range(3) : 
        for i2 in range(3, -1, -1) :
            if spaceship[i2][j] == '_' : 
                if spaceship[i][j] != '_' : 
                    spaceship[i2][j], spaceship[i][j] = spaceship[i][j], spaceship[i2][j]

print('\n'.join(''.join(row) for row in spaceship))