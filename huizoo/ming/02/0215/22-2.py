arr = [input() for _ in range(3)]
arr2 = set(arr)
if len(arr2)==1:
    print('WOW')
elif len(arr2)==2:
    print('GOOD')
else:
    print('BAD')