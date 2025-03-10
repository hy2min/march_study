T=int(input())

for tc in range(1,T+1):
    N=int(input())
    A=[]
    B=[]
    cnt=0
    for i in range(N):
        a,b=map(int,input().split())
        A.append(a)
        B.append(b)

    for i in range(N-1):
        for j in range(i+1,N):
            if (A[i] < A[j] and B[i] > B[j]) or (A[i] > A[j] and B[i] < B[j]):
                cnt+=1

    print(f'#{tc} {cnt}')




