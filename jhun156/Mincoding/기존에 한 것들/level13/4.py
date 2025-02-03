def main():
    a,b = map(int,input().split())
    SUM,GOP = ABC(a,b)
    print(SUM,GOP)

def ABC(num1,num2):
    return num1+num2,num1 * num2

main()