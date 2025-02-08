st = input()
n = len(st)
for i in range(n) : 
    for j in range(n-i-1, n) : 
        print(st[j], end = '')
    print()