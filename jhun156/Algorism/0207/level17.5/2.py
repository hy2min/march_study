arr = [3,7,4,1,2,6]

univer = [[i for i in map(int,input().split())] for _ in range(2)]

def isExist(num):
    for i in range(6):
        if num == arr[i]:
            return "OK"
    return "NO"

for i in range(2):
    for j in range(2):
        univer[i][j] = isExist(univer[i][j])
for i in range(2):
    print(*univer[i])