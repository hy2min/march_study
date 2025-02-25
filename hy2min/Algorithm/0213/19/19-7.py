input_arr = [list(map(int,input().split())) for _ in range(4)]
vect = [[0] * 3 for _ in range(4)]

for i in input_arr:
    vect[i[0]][i[1]] = 5

for i in vect:
    for j in i:
        print(j, end=" ")
    print()
