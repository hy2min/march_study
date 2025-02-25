arr = [0] * 5

index, age = map(int,input().split())
arr[index] = age

while age >= 0 or index <= 4:
    for i in range(5):
        if arr[i] == 0:
            print("_",end='')
        else:
            print(arr[i],end='')
    print()
    if index == 4:
        break
    else:
        arr[index+1] = age - 1
        arr[index] = 0
        index += 1
        age -= 1

