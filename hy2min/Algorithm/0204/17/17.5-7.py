levelTable = [
    [10, 20],
    [30, 60],
    [100, 150],
    [200, 300],
]

calories = list(map(int, input().split()))
arr = []
for level in levelTable:
    cnt = 0 
    for calorie in calories:
        if level[0] <= calorie <= level[1]:
            cnt += 1
        else:
            continue
    arr.append(cnt)

for i, c in enumerate(arr):
    print(f'lev{i}:{c}')