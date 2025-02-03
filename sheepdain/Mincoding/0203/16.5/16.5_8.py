arr=['A',7,9,'T','K','Q'],['M','I','N','C','O','D']
a,b=map(str,input().split())
def isExist(arr,n):
    for i in arr:
        if n in i:
            return print(f'{n} : 존재')
    return print(f'{n} : 없음')
isExist(arr,a)
isExist(arr,b)