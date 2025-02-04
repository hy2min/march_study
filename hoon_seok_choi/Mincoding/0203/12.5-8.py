arr = [[0]*3 for _ in range(3)]

a = int(input())

for i  in range(3) :
    for j in range(3) :
        if  i + j >= 2:
            arr[i][j] = a
            a +=1

for i  in range(3) :
    for j in range(3) :
        print(arr[i][j],end="")
    print()