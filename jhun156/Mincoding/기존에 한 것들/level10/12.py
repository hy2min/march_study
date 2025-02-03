def Input():

    a = int(input())

    return a

def CountDown(num):

    for i in range(num,0,-1):
        print(i,end=' ')

def main():

    CountDown(Input())

main()
