def main():
    a,b = map(int,input().split())
    return a,b

def BBQ(a,b):
    sum = a + b
    minus = a - b
    mul = a * b
    mok = a // b
    print(f"합:{sum}")
    print(f"차:{minus}")
    print(f"곱:{mul}")
    print(f"몫:{mok}")

t,k = main()
BBQ(t,k)