vect = [
    [3,7,4],
    [2,2,4],
    [2,2,5],
]
target = list(map(int, input().split()))
target_count = [0, 0, 0]
for k in range(3):
    for i in range(3):
        for j in range(3):
            if vect[i][j] == target[k]:
                target_count[k] += 1
print(target[target_count.index(max(target_count))])