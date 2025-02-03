arr = [
    [3,4,1],
    [2,1,4],
    [3,3,0],
]

cnt = 0

for i in arr:
    for j in i:
        if j % 2 == 1:
            cnt += 1

print(f"짝수 : {9-cnt}")
print(f"홀수 : {cnt}")
