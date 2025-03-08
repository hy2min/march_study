arr = [['A', 'B', 'C', 'D', 'E'],
       ['F', 'G', 'H', 'I', 'J'],
       ['K', 'L', 'M', 'N', 'O'],
       ['P', 'Q', 'R', 'S', 'T'],
       ['U', 'V', 'W', 'X', 'Y'],
       ]
a = input()
for i in range(5) : 
    for j in range(5) : 
        if arr[i][j] == a : 
            print(f'{i-2},{j-2}')