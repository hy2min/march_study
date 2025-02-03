arr = [['A',7,9,'T','K','Q'],['M','I','N','C','O','D']]
a , b = map(str, input().split())

def isExist():
    flagA = False
    flagB = False
    for row in arr:
        if a in row:
            flagA = True
        if b in row:
            flagB = True
    print(f"{a} : {'존재' if flagA else '없음'}")
    print(f"{b} : {'존재' if flagB else '없음'}")
isExist()