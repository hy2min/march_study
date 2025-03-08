town = [['C', 'D', 'A'],
        ['B', 'M', 'Z'],
        ['Q', 'P', 'O'],
        ]
black = list(input())
dat = [0] * 26

for row in town : 
    for person in row : 
        if person in black : 
            dat[ord(person)-65] += 1
print(f'{26-dat.count(0)}명')