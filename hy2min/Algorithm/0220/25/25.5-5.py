s = input()

alp = ''
num = ''

alpha_lst = []
digit_list = []

for i in s:
    if i.isdigit():
        if alp:
            alpha_lst.append(alp)
            alp = ''
        num += i
        
    elif i.isalpha():
        if num:
            digit_list.append(int(num) + 17)
            num = ''
        alp += i
if alp:
    alpha_lst.append(alp)
if num:
    digit_list.append(int(num)+17)

for i in range(len(alpha_lst)):
    print(alpha_lst[i]+'#'+str(digit_list[i]))
