def BBQ():
    arr = list(map(int, input().split()))
    a = max(arr)
    b = min(arr)
    return a, b

a, b = BBQ()
print(f'a={a}')
print(f'b={b}')
