arr=[]
for i in range(2):
    string = input()
    arr.append(string)

arr1 = [0]*12
for i in range(2):
    arr1[i] = arr[i]
    print(arr1[i] if arr1[i] != 0 else '', end = '')