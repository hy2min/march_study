a = input()
b = ord(a)
arr = []

for i in range(3):
    row = []
    for j in range(5):
        row.append(chr(b))
        b += 1
    arr.append(row)

arr[2][2] = arr[2][2].lower()
print(arr[2][2])