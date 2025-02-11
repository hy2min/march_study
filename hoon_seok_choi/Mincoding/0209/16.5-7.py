arr = [[0] * 4 for _ in range(7) ]

a= 1
for i in range(7) :
    for j in range(4) :
        arr[i][j] = a
        a+=1

bcd = list(map(int,input().split()))

for j in range(3) :
    for i in range(4) :
        arr[bcd[j]][i] = 0


for i in range(7) :
    for j in range(4) :
        print(arr[i][j],end=" ")
    print()