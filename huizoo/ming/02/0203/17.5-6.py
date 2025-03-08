password = [3,7,4,9]
input1 = list(map(int, input().split()))

def isSame(list1, list2) : 
    if list1 == list2 : 
        return 'pass'
    else : 
        return 'fail'

ret = isSame(password, input1)
print(ret)