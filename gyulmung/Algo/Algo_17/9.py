vect = [[3, 7, 4], [2, 2, 4], [2, 2, 5]]
target = list(map(int, input().split()))

def Check_vect(tar):
    count = 0
    for i in range(3):
        for j in range(3):
            if vect[i][j] == tar:
                count += 1
    return count

Max_num = -1e8
for i in range(len(target)):
    count = Check_vect(target[i])
    if Max_num < count:
        Max_num = count
        result = target[i]
print(result)