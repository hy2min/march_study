a, b = map(int, input().split())
arr = [[[i]*3 for i in [a, b]] for _ in range(3)]

for i in range(3) :
    print('\n'.join(' '.join(map(str, row)) for row in arr[i]))
    print()

print('\n\n'.join('\n'.join(' '.join(map(str, row)) for row in arr[i]) for i in range(3)))