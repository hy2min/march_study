arr = ['A', 'P', 'P', 'L', 'E', 'T']

string = list(map(str, input().split()))

counter = 0
for i in string:
    for j in arr:
        if i == j:
            counter += 1
print(f'{counter}개 맞추었습니다')