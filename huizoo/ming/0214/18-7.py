arr = [
    ['A','B','C'],
    ['A','G','H'],
    ['H','I','J'],
    ['K','A','B'],
    ['A','B','C'],
]
dat = [0]*26
for i in range(5):
    for j in range(3):
        dat[ord(arr[i][j])-65] += 1

for i in range(26):
    print(chr(i+65)*dat[i], end='')