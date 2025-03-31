check = "ABCDEF"

st = input()
dic = dict()
for i in st:
    if i.isupper():
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    else:
        i2 = i.upper()
        if i2 in dic:
            dic[i2] += 1
        else:
            dic[i2] = 1

for i in check:
    if i in dic:
        print(f'{i}:{dic[i]}')
    else:
        print(f'{i}:0')