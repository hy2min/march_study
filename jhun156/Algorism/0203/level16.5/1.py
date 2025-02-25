a,b,c = map(int,input().split())

for i in range(c):
    print(*range(a,b+1))