vect=list(map(int,input().split()))

dat=[0]*10

for i in vect:
    dat[i] += 1

while 1:
    for i in range(10):
        if dat[i] != 0:
            dat[i] -= 1
            print(i,end=" ")
            break
    if dat==[0]*10:
        break