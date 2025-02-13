arr = []


for i in range(2) :
    arr2 = [*input()]
    arr.append(arr2)

arr3 = [0]*12

arr = sum(arr,[])


for i in range(len(arr)):
    arr3[i] = arr[i]


for i in range(len(arr)):
    print(arr3[i],end="")