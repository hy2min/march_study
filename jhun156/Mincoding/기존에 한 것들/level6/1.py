A,B = 0, 0

def custom(a,b):
    a,b = input().split()
    return a, b

def output(a,b):
    print(a,b)

A, B = custom(A,B)
output(A,B)