num = int(input())
arr = [list(map(int,input().split())) for _ in range(5)]

start_num = 0
if num == 1:
    for i in range(5):
        for j in range(0,start_num + 1):
            print(arr[i][j],end=' ')
        start_num += 1
        print()
else:
    for i in range(5):
        for j in range(0,start_num + 5):
            print(arr[i][j],end=' ')
        start_num -= 1
        print()

