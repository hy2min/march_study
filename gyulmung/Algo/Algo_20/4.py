
n = int(input())

def bbq(level):

    if level == n + 6:
        print(level, end = " ")
        return
    
    bbq(level + 2)
    print(level, end = ' ')


bbq(n)