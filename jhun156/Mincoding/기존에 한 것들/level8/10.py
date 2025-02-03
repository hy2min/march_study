arr = [
    [4,3,1,1],
    [3,1,2,1],
    [0,0,1,2],
]

a = int(input())
count = 0

for i in range(3):
    for j in range(4):
        if arr[i][j] == a:
            count += 1

print(f"{count}개 존재합니다")