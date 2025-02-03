arr = [4,3,6,1,3,1,5,3]
count = 0
a = int(input())

for i in arr:
    if i == a:
        count += 1

print(f"숫자{a}개수는{count}개")