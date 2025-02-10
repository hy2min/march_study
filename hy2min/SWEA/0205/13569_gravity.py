T = int(input())
for idx in range(T):
    N = int(input())
    H = list(map(int, input().split()))
    max_fall = 0
    for i in range(N):
        fall = 0
        for j in range(i+1, N):

            if H[i] > H[j]:
                fall += 1
        max_fall = max(max_fall, fall)
    print(f'#{idx+1} {max_fall}')
