a,b = map(int, input().split())

def abc(n):
    print(n, end=" ")
    if n == b:
        return

    abc(n+1)
    print(n, end=" ")

abc(a)