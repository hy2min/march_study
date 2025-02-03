def Input():
    a = int(input())
    return a

def main():
    a,b,c = map(int,input().split())
    calc(a,b,c)

def calc(num1,num2,num3):
    print(num1+num2+num3)

main()