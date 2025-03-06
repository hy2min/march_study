n = int(input())
m = 2
i = 1
while n > i:
    i += m
    m += 1
if m % 2 == 0:
    print(f'{1+(i-n)}/{m-1-(i-n)}')
else:
    print(f'{m-1-(i-n)}/{1+(i-n)}')