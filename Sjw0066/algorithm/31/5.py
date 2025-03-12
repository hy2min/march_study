n=int(input())
lst=list(input().split())

cnt=0
for i in range(n-1):
    for j in range(i+1,n):
        if lst[i]+lst[j] == 'HITSMUSIC':
            cnt+=1

print(cnt)