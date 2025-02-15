st = input()
dat = [0] * 100
for char in st:
    dat[ord(char)] += 1

for i in range(100):
    if 1 <= dat[i]:
        print(chr(i), end='')

