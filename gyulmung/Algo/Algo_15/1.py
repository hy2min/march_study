str1 = str(input())
str2 = str(input())

Flag = True
for i in str1:
    for j in str2:
        if i != j:
            Flag = False
            break
if Flag:
    print('같음')
else:
    print('다름')