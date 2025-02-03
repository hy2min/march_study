arr = [
    ['D','A','T','A','W'],
    ['B','B','Q','K'],
]

a = int(input())
if a % 2 == 1:
    arr[0].sort()
else:
    arr[1].sort()

for i in range(2):
    for j in range(len(arr[i])):
        print(arr[i][j],end='')
    print()