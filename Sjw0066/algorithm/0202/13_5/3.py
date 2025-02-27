A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

for i in range(5):
        result=A[i]*B[i]+C[i]
        print(result,end=" ")