arr = [
    ['4', '5', '7', '1', '3', '2'], 
    ['D', 'F', 'Q', 'W', 'G', 'Z']
]

a = int(input())

a = str(a)
# a_point = [0,0]

for i in range(2) :
    for j in range(6) :
        if arr[i][j] == a :
            # a_point = [i,j]
            print(arr[i+1][j])
