a = 1

for _ in range(5):
    order = input()
    if order == 'up':
        a += 1
    else:
        a -= 1

if a > 0:
    print(a)
else:
    print('B', abs(a-1), sep='')

