a, b = map(int, input().split())

def bbq(a, b):
    print(a,end = ' ')
    if a == b:
        return
    bbq(a+1, b)
    print(a, end = " ")


bbq(a, b)