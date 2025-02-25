cardlist = list(input())

# print(ord("A"))  # A65 # a97 

DAT = [0] * 30

for i in range(len(cardlist)):
    DAT[ord(cardlist[i])-65] += 1
ans = 0
for i in range(30):
    if DAT[i] != 0:
        ans += 1
print(f"{ans}개")