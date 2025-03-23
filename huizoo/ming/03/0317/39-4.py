n = int(input())
arr = sorted(list(map(int, input().split())))
limit = 100
cnt = 0
for num in arr:
    limit -= num
    if limit < 0:
        break
    cnt += 1
print(cnt)
