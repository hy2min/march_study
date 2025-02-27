arr=[list(map(int,input().split())) for _ in range(3)]

answer=0
for i in range(3):
    for j in range(i+1):
        answer+=arr[i][j]

print(answer)
    