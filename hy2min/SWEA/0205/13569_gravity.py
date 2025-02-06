T = int(input())
for _ in range(T):
    N = int(input())
    H = list(map(int, input().split()))
    max_fall = 0
for i in range(N):
    for j in range(i+1, N):
        fall = 0 
        if H[i] > H[j]:
            fall += 1
    max_fall = max(max_fall, fall)
print(max_fall)