n = int(input())
arr = list(input().split())
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == 'HITSMUSIC':
            cnt += 1
print(cnt)