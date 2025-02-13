arr=[
    [[2,4],
     [1,5]],

    [[2,3],
     [3,6]],

    [[7,3],
     [1,5]],
]
n=int(input())
Max=-21e8
Min=21e8
for i in range(2):
    for j in range(2):
        if Max<arr[n][i][j]:
            Max=arr[n][i][j]
        if Min>arr[n][i][j]:
            Min=arr[n][i][j]

print(f'MAX={Max}')
print(f'MIN={Min}')