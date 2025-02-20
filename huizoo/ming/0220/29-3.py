arr = [list(map(int, input().split())) for _ in range(3)]
for row in arr:
    if len(set(row)) == 1:
        print(row[0])
    else:
        print('x')