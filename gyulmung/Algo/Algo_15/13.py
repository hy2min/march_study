arr = [['D', 'A', 'T', 'A', 'W'], ['B', 'B', 'Q', 'K']]
num = int(input())

if num % 2 == 1:
    arr[0]=sorted(arr[0])
else:
    arr[1]=sorted(arr[1])

for i in range(2):
    for j in arr[i]:
        print(j, end = "")
    print()