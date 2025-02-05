vect = [3,5,4,2,6,6,5]
bit = list(map(int, input().split()))

for i in range(len(bit)):
    if bit[i]:
        bit[i] = vect[i]

for i in range(len(bit)):
    if bit[i] != 0:
        bit[i] = 7
print("".join(map(str,bit)))