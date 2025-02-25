s = input()

def abc(n):
    print(s[n],end="")

    if n == 4:
        print()
        print(s[n],end="")
        return
    
    abc(n+1)

    print(s[n], end="")

abc(0)