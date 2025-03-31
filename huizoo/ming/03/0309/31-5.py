n = int(input())
arr = input().split()
cnt = 0
for i in range(n-1):
    left = arr[i]
    for j in range(i+1, n):
        if left+arr[j] == 'HITSMUSIC':
            cnt += 1
print(cnt)