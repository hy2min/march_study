arr = [[""]*5 for _ in range(5)]

v = 65

for i in range(5) :
    for j in range(5) :
        arr[i][j] = chr(v)
        v +=1

a = input()

for i in range(5) :
    for j in range(5) :
        if arr[i][j] == a :
            print(f"{i-2},{j-2}")
 
