arr = [
    [0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
maco = ['A','B','C','D','E','F','G','H']
n = input()
papa = -1
for i in range(8):
    if arr[i][maco.index(n)]:
        papa = i
if papa == -1:
    print('없음')
else:
    bro = []
    for i in range(8):
        if arr[papa][i]:
            if maco[i] != n:
                bro.append(i)
    if not bro:
        print('없음')
    else:
        for i in bro:
            print(maco[i], end=' ')