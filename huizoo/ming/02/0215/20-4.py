def abc(n):
    if n == a+6:
        print(n, end = ' ')
        return
    abc(n+2)
    print(n, end = ' ')
a = int(input())
abc(a)