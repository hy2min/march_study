town = [
    ['C','D','A'],
    ['B','M','Z'],
    ['Q','P','O'],
]
black = list(input())
dat = [0]*4
for i in range(4):
    for j in range(3):
        if black[i] in town[j]:
            dat[i] = 1
print(dat.count(1), '명', sep='')