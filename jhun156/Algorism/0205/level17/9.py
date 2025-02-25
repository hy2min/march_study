vect = [
    [3,7,4],
    [2,2,4],
    [2,2,5],
]

target = list(map(int,input().split()))

def isCount(num):
    result = 0
    for i in range(3):
        for j in range(3):
            if num == vect[i][j]:
                result += 1
    return num, result

lst = {}
for i in target:
    key,value = isCount(i)
    lst[key] = value
    
values = lst.values()
max_value = max(list(values))

for key,value in lst.items():
    if value == max_value:
        print(key)