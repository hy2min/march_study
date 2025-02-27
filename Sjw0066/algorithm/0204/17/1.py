arr=['M','T','K','C']

a= input()

def isExist(arr,a):
    if a in arr:
        print('발견')
    else:
        print('미발견')

isExist(arr,a)