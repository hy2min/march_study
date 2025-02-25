town = [
    ['C','D','A'],
    ['B','M','Z'],
    ['Q','P','O'],
]

black_list = list(input())
DAT = [0] * 27

for i in range(3):
    for j in range(3):
        DAT[ord(town[i][j])-65] += 1
ans = 0

for j in range(4):
    tmp = ord(black_list[j])-65
    if DAT[tmp] != 0:
        ans += DAT[tmp]

print(f"{ans}명")