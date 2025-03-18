N=int(input())
degari=list(map(int,input().split()))
case=int(input())
for i in range(case):
    command,con1,con2=input().split()
    if command=='alliance':
        union(con1,con2)
    else:
        pass

