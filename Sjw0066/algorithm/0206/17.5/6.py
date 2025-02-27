password=[3,7,4,9]

input1=list(map(int,input().split()))

def isSame(password,input1):
    flag=0
    for i in range(4):
        if password[i] == input1[i]:
            pass
        else:
            flag=1
    
    if flag==1:
        print('fail')
    else:
        print('pass')
isSame(password,input1)