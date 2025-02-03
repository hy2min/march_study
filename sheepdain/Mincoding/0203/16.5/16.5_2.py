arr=[['']*3 for i in range(6)]
a=ord('A')
for i in range(2,-1,-1):
    for j in range(5,-1,-1):
        arr[j][i]=chr(a)
        a+=1
y,x=map(int,input().split())
print(arr[y][x])