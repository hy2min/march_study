L = int(input())
N = int(input())
cake = [0] * L
dat = [0]*(N+1)
max1 = 0
max1_num = 0
for i in range(1, N+1):
    P, K = map(int, input().split())
    if max1 < K-P+1:
        max1 = K-P+1
        max1_num = i
    for j in range(P-1, K):
        if cake[j] == 0:
            cake[j] = i
for i in range(L):
    if cake[i]:
        dat[cake[i]] += 1
print(max1_num)
print(dat.index(max(dat)))