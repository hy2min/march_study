person1 = input()
person2 = input()

def isSame(a, b) : 
    if a == b : 
        return 1
    else : 
        return 0

ret = isSame(person1, person2)
if ret : 
    print('동명')
else : 
    print('남남')