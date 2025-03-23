arr = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    if len(set(arr[i])) == 1 :
        print(arr[i][0])
    else : 
        print('x')