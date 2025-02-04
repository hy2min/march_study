str1 = str(input())
str2 = str(input())

str1_re = sorted(str1, reverse = True)
str2_re = sorted(str2, reverse = False)

print(str1_re)
print(str2_re)


Flag = True
for i in range(len(str1_re)):
    if str1_re[i] != str2_re[i]:
        Flag = False
        print('거울문장아님')
        break
if Flag:
    print('거울문장아님')
    