a = int(input())

arr = []

for i in range(5) :
    arr2 = list(map(int,input().split()))
    arr.append(arr2)


if a == 1 :
    for i in range(5) :
        for j in range(i+1) :
            print(arr[i][j],end= " ")
        print()
elif a==2 :
    for i in range(5) :
        for j in range(5-i) :
            print(arr[i][j],end= " ")
        print()