str1=input()

cut=len(str1)//2

cut_str1=str1[:cut]
cut_str2=str1[cut:]

if cut_str1 == cut_str2 :
    print('동일한문장')
else:
    print('다른문장')
