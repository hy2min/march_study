st_arr = list(map(str, input().split()))

for i in range(5):
    for j in range(5):
        if j + i < 5:
            print(st_arr[j + i], end = " ")
    print()