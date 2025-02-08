vect = "MINCODING"

n = int(input())
target = [i for i in input().split()]

DAT = [0] * 27
for i in range(len(vect)):
    DAT[ord(vect[i])-65] += 1

for i in range(n):
    if DAT[ord(target[i])-65] != 0:
        print("O",end='')
    else:
        print("X",end='')