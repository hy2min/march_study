string = list(input())
DAT = [0] * 27

for i in range(len(string)):
    DAT[ord(string[i])-65] += 1

for i in range(27):
    if DAT[i] != 0:
        print(f"{chr(i+65)}:{DAT[i]}")