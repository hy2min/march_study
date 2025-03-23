a, b = 0, 0
p1, p2 = a, b

def BBQ(a, b) : 
    numbers = list(map(int, input().split()))
    a = max(numbers)
    b = min(numbers)
    return a, b

ret1, ret2 = BBQ(a, b)
print(f'a={ret1}')
print(f'b={ret2}')
