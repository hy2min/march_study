N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[1])
cnt = 0
ed = 0
for start, end in arr:
    if start >= ed:
        cnt += 1
        ed = end

print(cnt)