arr = []
len_arr = []
for i in range(4):
    string = input()
    arr.append(string)

for i in range(4):
    len_arr.append(len(arr[i]))

len_arr.sort()
print(*len_arr)