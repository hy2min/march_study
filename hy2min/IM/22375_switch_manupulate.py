T = int(input())
for idx in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if A[i] != B[i]:
            cnt +=1
            for j in range(i, N):
                if A[j] == 0:
                    A[j] = 1
                else:
                    A[j] = 0
    print(f'#{idx+1} {cnt}')
