n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1],x[0]))
prev_end = 0
cnt = 0
for start, end in arr:
    if prev_end <= start:
        cnt += 1
        prev_end = end
print(cnt)