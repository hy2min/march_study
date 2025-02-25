a = input()
DAT = [0] * 27

for i in range(len(a)):
    DAT[ord(a[i])-65] += 1

for i in range(27):
    if DAT[i] != 0:
        print(chr(i+65),end='')
        DAT[i] = 0
