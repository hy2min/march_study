def main():
    
    a,b = map(int,input().split())

    if (a // b) % 2 == 0:
        even(a//b)
    else:
        odd(a//b)

    printData(a+b) 

def even(num):

    rnt = 2 * num
    printData(rnt)

def odd(num):

    rnt = num - 10
    printData(rnt)

def printData(num):
    print(num)

main()