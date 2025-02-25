s = input()
l = len(s)

def abc(n):
    print(n, end=" ")
    if n == 1:
        return
    abc(n-1)
    print(n, end=" ")

abc(l)