a = "BBQWORLD"
b = "KFCAPPLE"
c = "LOT"

A = input()
lst= [a,b,c]

count = 0
for i in range(3):
    for j in range(len(lst[i])):
        if A == lst[i][j]:
            count += 1
print(count)