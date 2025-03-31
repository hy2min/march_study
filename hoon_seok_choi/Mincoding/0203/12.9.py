arr = [[0] *5 for _ in range(5)]

a, b =input().split()

a = int(a) - 1  
b = b.upper() 

for i in range(5):
    arr[a][i] = chr(ord(b) +4 - i)

for i in range(5):
    for j in range(5):
        if arr[i][j] == 0: 
            print(0, end="")
        else:
            print(arr[i][j], end="")
    print()