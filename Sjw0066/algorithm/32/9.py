str1=list(map(str,input()))
N=int(input())

sorted_str=list(sorted(str1,reverse=True))
result=sorted_str[:N]

Max=-21e8
for i in range(N):
    cnt = 0
    for j in range(i+1,N):
        if result[i]==result[j]:
            cnt+=1
            if cnt>=Max:
                idx=i
                Max=cnt

print(result[idx])
