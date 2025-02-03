arr1 = [3,5,2,4,1]
arr2 = [
    [9,8],
    [7,1],
    [3,4],
]

a = int(input())

if a % 2 == 1:
    for i in arr1:
        print(i,end='')
else:
    for i in arr2:
        for j in i:
            print(j,end='')
        print()