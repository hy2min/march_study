arr=[[['A','T','B'],['C','C','B']],[['A','A','A'],['B','B','C']]]

str1=input()
flag=0
for i in arr:
    for j in i:
        if str1 in j :
            flag=1


if flag:
    print('발견')
else:
    print('미발견')