arr=[list(input()) for _ in range(4)]

flagA=0
flagB=0
for i in arr:
    
    if 'A' in i :
        flagA=1
    elif 'B' in i :
        flagB=1

flag=flagA+flagB     

if flag == 2:
   print('대발견')
elif flag ==1 :
   print('중발견')
else:
   print('미발견')  
