arr = [
    [3, 7, 4],
    [2, 2, 4],
    [2, 2, 5]
]

target = list(map(int, input().split()))

cnt=0

max_v = -21e8


for i in range(3) :
    for j in range(3) :
        if target[i] in arr[j] :
            cnt+=1
    if cnt > max_v :
        max_v = cnt
    cnt = 0

print(max_v)
