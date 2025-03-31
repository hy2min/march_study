T=int(input())
for tc in range(1,T+1):
    A,B=map(str,input().split())

    cnt=0
    for i in range(len(A)):
        flag=0
        for j in range(len(B)):
            if i+j > len(A)-1:
                continue
            if A[i+j] == B[j]:
                flag+=1
        if flag==len(B):
            cnt+=1

    answer=len(A)-cnt*len(B)+cnt
    print(f'#{tc} {answer}')