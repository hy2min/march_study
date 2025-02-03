arr = [
    ['A','B','C','D','E','F','G'],
    [4,2,5,1,6,7,3],
]

lst = [i for i in input().split()]
arr2 = []

for i in range(7):
    for j in range(2):
        if arr[0][i] == lst[j]:
            arr2.append(i)

a = arr2[0]
b = arr2[1]

SUM = 0
if a > b:
    for i in range(b+1,a):
        SUM += arr[1][i]
else:
    for i in range(a+1,b):
        SUM += arr[1][i]
print(SUM)