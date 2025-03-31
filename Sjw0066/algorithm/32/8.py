N=int(input())
result=[]

for i in range(N):
    flag1 = 0
    flag2 = 0
    str1=input()
    if str1[0].isupper():
        for j in range(1,len(str1)):
            if str1[j].islower():
                flag1+=1
        if flag1==len(str1)-1:
            result.append(str1)
        else:
            result.append(str1.upper())
    else:
        for j in range(1,len(str1)):
            if str1[j].isupper():
                flag2+=1
        if flag2:
            result.append(str1.upper())
        else:
            temp = str1[0].upper() + str1[1:]
            result.append(temp)





result.sort()
for i in result:
    print(i)