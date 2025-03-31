import sys
sys.stdin = open('input.txt','r')

n = int(input())
arr = list(input().split())
cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] + arr[j] == 'HITSMUSIC':
            cnt += 1
print(cnt)