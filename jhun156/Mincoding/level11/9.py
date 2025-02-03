arr = [i for i in input().split()]

big = []
small = []

for i in arr:
    if i.isupper():
        big.append(i)
    else:
        small.append(i)

BIG = ""
SMALL = ""

for i in range(len(big)):
    BIG += big[i]
for i in range(len(small)):
    SMALL += small[i]

print(f"big={BIG}\nsmall={SMALL}")