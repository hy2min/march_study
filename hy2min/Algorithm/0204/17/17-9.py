vect = [
    [3, 7, 4],
    [2, 2, 4],
    [2, 2, 5],
]

target = list(map(int, input().split()))

cnt_list = []
for n in target:
    cnt = 0
    for row in vect:
        cnt += row.count(n)
    cnt_list.append(cnt)

answer = target[cnt_list.index(max(cnt_list))]

print(answer)