arr=[['A',7,9,'T','K','Q'],['M','I','N','C','O','D']]

a,b=map(str,input().split())
def isExist(arr,a,b):
    flagA=0
    flagB=0

    for i in arr:
        if a in i :
            flagA = 1
        if b in i :
            flagB = 1
    
    if flagA == 1:
        print(f'{a} : 존재')
    else:
        print(f'{a} : 없음')    
    
    if flagB == 1:
        print(f'{b} : 존재')
    else:
        print(f'{b} : 없음')    
    
isExist(arr,a,b)