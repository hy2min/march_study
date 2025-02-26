arr = [[3, 5, 9], [4, 2, 1], [5, 1, 5]]

numbers = list(map(int, input().split()))

def isExist(num):
    for i in arr:
        for j in i:
            if j == num:
                return f'{num}:존재'
    return f'{num}:미발견'

for i in range(len(numbers)):
    print(isExist(numbers[i]))