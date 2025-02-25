arr = [
    [3,5,4,1],
    [1,1,2,3],
    [6,7,1,2],
]
numbers = list(map(int, input().split()))

# arr2 = [
#     [3,5,4,1],
#     [1,1,2,3],
#     [6,7,1,2],
# ]
# for i in range(3) : 
#     for j in range(4) : 
#         for k in range(4) : 
#             if arr[i][j] == numbers[k] : 
#                 if k < 3 : 
#                     arr2[i][j] = numbers[k+1]
#                 else : 
#                     arr2[i][j] = numbers[0]

# print('\n'.join(' '.join(map(str, row)) for row in arr2))


dic = {numbers[i]:numbers[(i+1)%4] for i in range(4)}

arr = [[dic.get(value, value) for value in row] for row in arr]

print('\n'.join(' '.join(map(str, row)) for row in arr))