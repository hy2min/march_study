str1=input()
str2=input()
str3=input()

flag1=1
flag2=1
flag3=1

if len(str1)==len(str2):
    for i in range(len(str1)):
        if str1[i] != str2[i] :
            flag1 = 0
else:
    flag1=0

if len(str2) == len(str3):
    for i in range(len(str2)):

        if str2[i] != str3[i]:
            flag2 = 0
else:
    flag2=0

if len(str1) == len(str3):
    for i in range(len(str1)):
        if str1[i] != str3[i]:
            flag3 = 0
else:
    flag3=0

flag=flag1+flag2+flag3

if flag == 3:
    print('WOW')
elif flag ==0:
    print('BAD')
else:
    print('GOOD')


