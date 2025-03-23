n1, n2, a = input().split()
n1, n2 = int(n1), int(n2)

for k in range(2):
    for i in range(n1):
        for j in range(n2):
            print(a, end='')
        print()
    print()
