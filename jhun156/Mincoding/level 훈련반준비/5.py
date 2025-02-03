a,b,c = map(int,input().split())

for i in range(c):
    num = a
    for i in range(b):
        print(num, end = ' ')
        num += 1
    print()