arr = []

for i in range(2):
    row = []
    row.extend(list(input()))
    arr.append(row)

result_list = []
for i in range(2):
    for j in range(len(arr[i])):
        result_list.append(arr[i][j])

for i in result_list:
    print(i,end='')