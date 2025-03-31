N,M = map(int,input().split())

cards= list(map(int,input().split()))

max_sum=M
answer=0
sum1=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum1 = cards[i]+cards[j]+cards[k]
            if sum1 > max_sum :
                continue
            else:
                if sum1>answer:
                    answer=sum1

print(answer)