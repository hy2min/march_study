level = int(input())
branch = int(input())

def abc(n):
    if n == level:
        return

    for i in range(branch):
        abc(n+1)

abc(0)