N, M = map(int, input().split())
card = list(map(int, input().split()))

min_diff = M
sum_card = 0
for i in range(N) : 
    for j in range(N) : 
        if i != j :
            for k in range(N) : 
                if i != k and j != k : 
                    temp = card[i]+card[j]+card[k]
                    if 0 <= M - temp < min_diff : 
                        min_diff = M - temp
                        sum_card = temp
print(sum_card)