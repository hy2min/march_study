arr = [list(input()) for _ in range(3)]
dat = [0] * 100
for row in arr : 
    for char in row:
        dat[ord(char)] += 1
if max(dat) == 1:
    print('Perfect')
else :
    print('No')