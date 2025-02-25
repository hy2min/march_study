arr = ['A','P','P','L','E','T']

lst = [i for i in input().split()]
count = 0

for i in lst:
    for j in arr:
        if i == j:
            count += 1
print(f"{count}개 맞추었습니다")