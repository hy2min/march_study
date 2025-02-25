women = [int(input()) for _ in range(5)]

max_age = -21e8
min_age = 21e8

for age in women:
    if age > max_age:
        max_age = age
    if age < min_age:
        min_age = age
print(f'MAX:{max_age}')
print(f'MIN:{min_age}')