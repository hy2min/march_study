a,b = map(int,input().split())

def abc(num1,num2):

    print(num1,end=' ')
    if num1 == num2:
        return
    abc(num1+1,num2)
    print(num1,end=' ')

abc(a,b)