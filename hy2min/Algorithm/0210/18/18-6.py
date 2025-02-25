town = [
    ['C','D','A'],
    ['B','M','Z'],
    ['Q','P','O'],
]
black = list(input())
black_cnt = [0] * 26
for alps in town:
    for alp in alps:
        black_cnt[ord(alp)-65] += 1
cnt = 0
for i in range(26):
    if black_cnt[i] > 0 and chr(i+65) in black:
        cnt += 1
print(f'{cnt}명')
