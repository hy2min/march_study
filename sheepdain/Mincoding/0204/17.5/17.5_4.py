arr=['G','K','T'],['P','A','C']
a,b=input().split()

def isExist(a,b):
    aCount=0
    bCount=0
    for i in arr:
        for j in i:
            if a==j:
                aCount+=1
            if b==j:
                bCount+=1
    if (aCount and bCount) != 0:
        print('대발견')
    elif (aCount or bCount) !=0:
        print('중발견')
    else:
        print('미발견')
isExist(a,b)