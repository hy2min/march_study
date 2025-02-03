a = int(input())

def BBQ(num):

    for i in range(1,num+1):
        print(i,end='')

def KFC(chr):

    print(chr * 7)

if a % 2 == 1:
    number = int(input())
    BBQ(number)
else:
    mun = input()
    KFC(mun)

