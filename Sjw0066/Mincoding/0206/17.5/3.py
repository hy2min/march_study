name1=input()
name2=input()

def isSame(name1,name2):
    if len(name1) == len(name2):
        for i,j in zip(name1,name2):
            if i != j :
                return 0
    else:
        return 0
    
    return 1

flag=isSame(name1,name2)
if flag:
    print('동명')
else:
    print('남남')
