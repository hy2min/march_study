def abc(n):
    print(n,end=' ')
    if n==b:
        return
    abc(n+1)
    print(n,end=' ')

a,b=map(int,input().split())
abc(a)