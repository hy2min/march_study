arr = [
    ['G', 'K', 'G'],
    input().split()
]
dat = [0]*26
for row in arr : 
    for alp in row : 
        dat[ord(alp)-65] += 1
if max(dat) >= 3 : 
    print('있음')
else : 
    print('없음')