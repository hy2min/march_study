n = int(input())

def bungee(n):
    print(n, end=" ")
    if n == 0:
        return
    bungee(n-1)
    print(n, end=" ")
bungee(n)