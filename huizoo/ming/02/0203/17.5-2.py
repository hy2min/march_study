arr = [3,7,4,1,2,6]
univer = [list(map(int, input().split())) for _ in range(2)]

for lst in univer : 
    for elem in lst : 
        if elem in arr : 
            print('OK', end = " ")
        else : 
            print('NO', end = " ")
    print()
