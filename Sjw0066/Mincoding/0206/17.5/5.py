vect=[3,5,4,2,6,6,5]

bit = list(map(int,input().split()))


for i in range(7):
    if bit[i]:
        pass
    else:
        vect[i] = 0

for i in range(7):
    if vect[i]:
        print(7,end="")
    else:
        print(0,end="")