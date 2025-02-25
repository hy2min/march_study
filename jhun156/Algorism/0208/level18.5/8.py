lst = []    # a,b,c 
for i in range(3):
    lst.append(input())

DAT = [0] * 27

for i in range(3):
    for j in range(len(lst[i])):
        DAT[ord(lst[i][j])-65] += 1

flag = 0
for i in range(27):
    if DAT[i] != 0 and DAT[i] != 1:
        flag = 1
        break

if flag == 1:
    print("No")
else:
    print("Perfect")