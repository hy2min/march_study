def CountDown(n):
    print(n,end=' ')
    if n==0: return
    CountDown(n-1)
    print(n,end=' ')

n=int(input())
CountDown(n)