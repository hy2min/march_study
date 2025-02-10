arr=['A','T','K','B'],['C','Z','F','D'],['H','G','E','I']
a,b,c=input().split()
y=int(b)
x=int(c)
def Offset(arr,a,y,x):
    for i in range(3):
        for j in range(4):
            if arr[i][j]==a:
                return arr[i+y][j+x]
print(Offset(arr,a,y,x))