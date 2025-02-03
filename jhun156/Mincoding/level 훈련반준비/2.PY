arr = [
    [5,1,4,2,6],
    [3,5,0,0,7],
    [9,9,8,3,1],
]

a = int(input())

count = 0

for i in range(3):
    for j in range(5):
        if arr[i][j] > a:
            count += 1

print(f"{count}개")