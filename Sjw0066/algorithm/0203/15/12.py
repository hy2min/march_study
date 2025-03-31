arr=[list(input()) for _ in range(2)]

arr2=[0]*12

for i in range(len(arr[0])):
   arr2[i] = arr[0][i]

for i in range(len(arr[0]),len(arr[0])+len(arr[1])):
   arr2[i] = arr[1][i-len(arr[0])]

print(''.join(list(filter(bool,arr2))))