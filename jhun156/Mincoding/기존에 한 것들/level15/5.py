arr = [[0] * 6 for _ in range(4)]
a = input()
b = input()
c = input()
d = input()
lst = [a,b,c,d]

for i in range(4):
    for j in range(len(lst[i])):
        arr[i][j] = lst[i][j]

result_list = []

for i in range(4):
    count = 0
    for j in range(6):
        if arr[i][j] != 0:
            count += 1
    result_list.append(count)

result_list.sort()
print(*result_list)