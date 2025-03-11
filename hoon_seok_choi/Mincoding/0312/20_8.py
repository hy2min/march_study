n = int(input())

def recur(n):
    if n == 0:
        return
    
    recur(n // 2)
    print(n,end=" ")

recur(n)