str1 = input()
str2 = input()

str1_rev = ''.join(list(reversed(list(str1))))

if str1_rev == str2 :
    print('거울문장')
else:
    print('거울문장아님')