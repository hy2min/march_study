arr = [i for i in input().split()]
start_num = 0
for i in range(5):
    for j in range(start_num,5):
        print(arr[j],end=' ')
    start_num += 1
    print()