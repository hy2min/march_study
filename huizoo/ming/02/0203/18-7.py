arr = [['A', 'B', 'C'],
       ['A', 'G', 'H'],
       ['H', 'I', 'J'],
       ['K', 'A', 'B'],
       ['A', 'B', 'C'],
       ]

dat = [0]*26

for row in arr : 
    for alp in row : 
        dat[ord(alp)-65] += 1

print(''.join(chr(i+65)*dat[i] for i in range(26)))