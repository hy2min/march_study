vect = [3,5,4,2,6,6,5]
bit = list(map(int, input().split()))
for i in range(7):
    if bit[i]:
        vect[i] = 7
    else :
        vect[i] = 0
print(*vect,sep='')
