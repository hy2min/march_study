arr = [list(map(int, input().split())) for _ in range(4)]

max_cnt = -21e8
for i in range(len(arr)):
    cnt = arr[i].count(1)
    if cnt > max_cnt:
        max_cnt = cnt
        max_idx = i
print(chr(max_idx+65))