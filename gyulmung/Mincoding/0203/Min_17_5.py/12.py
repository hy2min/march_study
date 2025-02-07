lst = []
count = 0
for i in range(5):
    arr = []
    for j in range(5):
        arr.append(chr(ord('A')+count))
        count += 1
    lst.append(arr)
print(lst)

st = input()

for i in range(5):
    for j in range(5):
        if lst[i][j] == st:
            y, x = i-2, j-2
print(y, x)