arr=[[0]*4 for i in range(7)]
n=1
for i in range(7):
    for j in range(4):
        arr[i][j]=n
        n+=1
a,b,c=map(int,input().split())
arr[a]=[0]*4
arr[b]=[0]*4
arr[c]=[0]*4
for i in arr:
    print(*i)