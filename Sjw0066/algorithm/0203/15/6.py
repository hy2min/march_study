str1 = input()

flag=0

for i in range(len(str1)-1):
    if str1[i].isupper() == str1[i+1].isupper():
        flag=1
        break

if flag==1:
    print("일반문장")
else:
    print("개구리문장")
