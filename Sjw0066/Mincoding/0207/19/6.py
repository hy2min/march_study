

class win:
    def __init__(self,age,name):
        self.age=age
        self.name=name

def isSameName(str1,str2):
    for i in range(len(str1)):
        if str1[i] != str2[i] :
            return False

    return True

def isSameAge(int1,int2):
    
    if int1 != int2 :   
        return False

    return True
c1,c2,c3,c4,c5,c6,c7 = win(15, "summer"),win(33, "cloe"),win(24, "niki"),win(28, "niki"),win(32, "jenny"),win(20, "summer"),win(40, "coco")

train=[c1,c2,c3,c4,c5,c6,c7]

input1=input()
input2=int(input())

for i in range(len(train)):
    flag1=isSameName(train[i].name,input1)
    flag2=isSameAge(train[i].age,input2)
    if flag1 & flag2:
        print(i)