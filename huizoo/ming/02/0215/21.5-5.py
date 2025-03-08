arr = list(map(int, input().split()))
bucket = [0]*10
for i in arr:
    bucket[i] += 1

for i in range(10):
    if bucket[i]:
        print(f'{i} '*bucket[i], end='')