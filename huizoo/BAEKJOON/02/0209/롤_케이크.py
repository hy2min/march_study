L = int(input())
N = int(input())
aud = [list(map(int, input().split())) for _ in range(N)]
cake = [0]*L

P, K = max(aud, key = lambda x : x[1]-x[0])
print(aud.index([P, K])+1)

for i in range(N) : 
    for j in range(aud[i][0]-1, aud[i][1]) : 
        if cake[j] == 0:
            cake[j] = i+1

dat = [0]*(N+1)
for i in range(L) : 
    if cake[i] : 
        dat[cake[i]] += 1

print(dat.index(max(dat)))