# import sys
# sys.stdin = open('input.txt','r')
T=int(input())

for tc in range(1,T+1):
    if tc==2:
        pass

    N,M=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if N>M:
        N,M=M,N
        short=b
        long=a
    else:
        short=a
        long=b

    max_mul=-21e8

    for i in range(abs(M-N)+1):
        mul = 0
        for j in range(N):
            mul+=short[j]*long[i+j]
        if mul>max_mul:
            max_mul=mul

    print(f'#{tc} {max_mul}')