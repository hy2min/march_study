arr=[['G','K','T'],['P','A','C']]

str1,str2=map(str,input().split())



def isExist():
    cnt=0
    for i in arr:
        for j in i:
            if j == str1 or j==str2:
                cnt+=1
    return cnt
result=isExist()        
if result==2:
    print('대발견')
elif result ==1 :
    print('중발견')
else:
    print('미발견')