arr = [10,50,40,20,30,40]

input_arr = [i for i in map(int,input().split())]

for i in range(6):
    count = 0
    for j in range(6):
        if arr[j] > input_arr[i]:
            count += 1
    print(f"{input_arr[i]}={count}개")
