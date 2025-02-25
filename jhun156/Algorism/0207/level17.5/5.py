vect = [3,5,4,2,6,6,5]

bit = [i for i in map(int,input().split())]

for i in range(7):
    if bit[i] == 0:
        vect[i] = 0

for i in range(7):
    if vect[i] != 0:
        print("7",end='')
    else:
        print("0",end='')