arr=['M','T','K','C']
a=input()
def isExist(a):
    for i in arr:
        if i==a:
            return print('발견')
    return print('미발견')
isExist(a)