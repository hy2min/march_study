def abc(t):
    if t==a:
        print(t,end=' ')
        return
    abc(t+2)
    print(t,end=' ')

n=int(input())
a=n+6
abc(n)