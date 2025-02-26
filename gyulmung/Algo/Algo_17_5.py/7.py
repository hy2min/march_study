level = [[10, 20], [30, 60], [100, 150], [200, 300]]

calories = list(map(int, input().split()))
lst = [0]*4

def cal_level(fat):
    for i in range(4):
        for j in range(1):
            if level[i][j] <= fat <= level[i][j+1]:
                return i


for i in range(len(calories)):
    result = cal_level(calories[i])
    lst[result] += 1

for i in range(len(lst)):
    print(f'lev{i}:{lst[i]}')

