a = input()

arr = [[0]*3 for _ in range(3)]

a = ord(a)

for i in range(2,-1,-1) :
    for j in range(3-i) :
        if i+j <= 3:
            arr[i][j] = a
            a +=1

for i in range(3) :
    for j in range(3-i) :
        print(chr(arr[i][j]),end="")
    print()