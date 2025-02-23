arr = [[0]*5 for _ in range(5)]

a = int(input())

for i in range(5) :
    for j in range(5) :
        if i == 0 or i == 4 or j ==0 or j==4 :
            arr[i][j] = a
        else :
            arr[i][j] = "_"



for i in range(5) :
    for j in range(5) :
        print(arr[i][j],end="")
    print()