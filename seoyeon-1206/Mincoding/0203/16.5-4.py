a,b =map(int, input().split())
lst = [0] * 6
lst[0] = a
lst[1] =b
for i in range(2,6):
    lst[i] = lst[i-2] * lst[i-1]
print(lst[-1])