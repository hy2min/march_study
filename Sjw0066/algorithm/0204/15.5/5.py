a,b,c = map(int,input().split())

rst=[]
for i in range(a,a+b):
    rst.append(i)

for i in range(c):
    print(*rst)