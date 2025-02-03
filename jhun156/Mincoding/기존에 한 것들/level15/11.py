arr = []

for i in range(4):
    row = []
    row.extend(list(input()))
    arr.append(row)
a,b = 0,0

for i in range(4):
    for j in range(len(arr[i])):
        if arr[i][j] == 'A':
            a = 1
        elif arr[i][j] == 'B':
            b = 1

if a == 1 and b == 1:
    print("대발견")
elif a ==1 or b == 1:
    print("중발견")
else:
    print("미발견")