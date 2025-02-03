def main():
    a = int(input())
    age1,age2,age3 = moom(a)
    print(age1,age2,age3)

def moom(num):
    a = num - 4
    b = num + 3
    c = num * 2
    return a,b,c

main()