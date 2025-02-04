MAP=[3,55,42],[-5,-9,-10]
pix=[]
for i in range(2):
    pix.append(list(map(int,input().split())))
# for i in range(2):
#     for j in range(2):
#         for h in map:
#             if pix[i][j] in h:


def isIn(n):
    for h in MAP:
        if n in h:
            return 'Y'
    return 'N'
for i in range(2):
    for j in range(2):
        pix[i][j]=isIn(pix[i][j])
for i in pix:
    print(*i)
print(*pix,sep='\n')