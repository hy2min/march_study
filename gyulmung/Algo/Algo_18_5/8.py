string1 = list(input())
string2 = list(input())
string3 = list(input())

lst = [0]*26

for i in range(len(string1)):
    lst[ord(string1[i])-65] += 1

for i in range(len(string2)):
    lst[ord(string2[i])-65] += 1

for i in range(len(string3)):
    lst[ord(string3[i])-65] += 1

Flag = False
for i in lst:
    if i >= 2:
        Flag = True

if Flag:
    print('No')
else:
    print('Perfect')