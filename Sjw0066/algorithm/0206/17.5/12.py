arr=[[0]*5 for _ in range(5)]
target=input()

ord_start=65
for i in range(5):
    for j in range(5):
        arr[i][j] = chr(ord_start)
        ord_start+=1

for i in range(5):
    for j in range(5):
        if target == arr[i][j] :
            print(f'{i-2},{j-2}')