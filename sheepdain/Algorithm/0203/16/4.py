A=[0]*4
B=[0]*4
A=list(map(int,input().split()))
B=list(map(int,input().split()))
result=[]
i,j=0,3
while i<=3:
    result.append(A[i]+B[j])
    i+=1
    j-=1
for i in result:
    print(i,end=' ')