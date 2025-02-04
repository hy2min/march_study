arr=[['A','T','K','B'],['C','Z','F','D'],['H','G','E','I']]

lst1=list(map(str,input().split()))

a=lst1[0]

b=int(lst1[1])
c=int(lst1[2])

x=0
y=0
for i in range(3):
    for j in range(4):
        if arr[i][j] == a:
            x,y=i,j


x=x+b
y=y+c

print(arr[x][y])
    