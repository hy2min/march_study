st = input()
length = len(st)

def rec(n) : 
    print(n, end = ' ')
    if n > 1 : 
        rec(n-1)
        print(n, end = ' ')

rec(length)

