from collections import Counter

s = input().upper()

dic = Counter(s)

for i in range(65,71):
    print(f'{chr(i)}:{dic[chr(i)]}')