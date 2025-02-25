arr = [[0]*3 for _ in range(2)]

inputs = list(map(int, input().split()))
if len(inputs) < 6 : 
    inputs2 = list(map(int, input().split()))
    arr[0] = inputs
    arr[1] = inputs2
else : 
    arr[0] = inputs[:3]
    arr[1] = inputs[3:]

arr2 = []

for i in range(2) : 
    arr2.extend(arr[i])

arr2.sort()

for i in range(2) : 
    arr[i] = arr2[3*i:3*i+3]

print('\n'.join(' '.join(map(str, row)) for row in arr))