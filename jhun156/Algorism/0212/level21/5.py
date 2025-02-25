arr = []
for i in range(3):
    a = input()
    arr.append(a)

Max = 0
for i in range(3):
    if len(arr[i]) > Max:
        Max = len(arr[i])
for i in range(3):
    if len(arr[i]) == Max:
        arr[i],arr[0] = arr[0],arr[i]

for i in range(3):
    print(arr[i])