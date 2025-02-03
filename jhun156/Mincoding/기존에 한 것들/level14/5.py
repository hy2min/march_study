arr = [[i for i in map(int,input().split())] for _ in range(3)]
sum = 0
end_point = 1
for i in range(3):
    for j in range(0,end_point):
        sum += arr[i][j]
    end_point += 1
print(sum)