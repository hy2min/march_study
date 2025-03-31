N = int(input())
arr = list(input().split())
cnt = 0
for i in range(N):
    for j in range(i+1,N):
        if arr[i] + arr[j] == 'HITSMUSIC':
            cnt += 1

print(cnt)