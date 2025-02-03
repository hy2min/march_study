def Sum(num1,num2):
    return num1+num2

def Comp(num1,num2):
    return num1-num2

def Print(num1,num2):
    print(f"합:{num1}\n차:{num2}")

def main():
    a,b = map(int,input().split())

    sum = Sum(a,b)
    comp = Comp(a,b)
    Print(sum,comp)

main()

