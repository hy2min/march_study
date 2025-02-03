a= int(input())

arr = [[" "]*4 for _ in range(3)]

for i in range(3) :
    for j in range(2-i,4) :
        arr[i][j] = str(a)
        a += 1


for i in range(3) :
    for j in range(4) :
        print(arr[i][j],end="")
    print()


