arr = [
    ['A','7','9','T','K','Q'],
    ['M','I','N','C','O','D'],
    ]

str1, str2 = input().split()
flag1 = False
flag2 = False
for i in arr:
    if str1 in i:
        flag1 = True
    if str2 in i:
        flag2 = True

if flag1:
    print(f'{str1} : 존재')
else:
    print(f'{str1} : 없음')

if flag2:
    print(f'{str2} : 존재')
else:
    print(f'{str2} : 없음')