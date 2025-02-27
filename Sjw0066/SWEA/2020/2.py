a=[list(map(int,input().split())) for _ in range(3)]
blank=input()
b=[list(map(int,input().split())) for _ in range(3)]


lst1=b[0]
lst2=[b[0][0]]+[b[1][0]]+[b[2][0]]
lst2=lst2[::-1]
lst3=b[2][::-1]
lst4=[b[0][2]]+[b[1][2]]+[b[2][2]]

answer=0
if a[0] == lst1:
    answer=0
elif a[0] ==lst2:
    answer=1
elif a[0] ==lst3:
    answer=2
elif a[0]==lst4:
    answer=3

print(answer)