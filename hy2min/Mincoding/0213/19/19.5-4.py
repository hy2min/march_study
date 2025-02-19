arr = [[0] * 4 for _ in range(4)]
for _ in range(3):
    l, idx = input().split()
    if l == 'G':
        for i in range(4):
            arr[int(idx)][i] = 1

    elif l == 'S':
        for i in range(4):
            arr[i][int(idx)] = 1

for i in arr:
    for j in i:
        print(j, end=" ")
    print()
