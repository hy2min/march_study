arr = [[0]*4 for _ in range(4)]
for _ in range(3):
    a, n = input().split()
    n = int(n)
    if a == 'G':
        arr[n] = [1]*4
    else:
        for i in range(4):
            arr[i][n] = 1

print('\n'.join(' '.join(map(str, row)) for row in arr))