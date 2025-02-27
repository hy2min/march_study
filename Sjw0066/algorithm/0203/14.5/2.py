triangle=int(input())

arr= [list(map(int,input().split())) for _ in range(5)]



if triangle==1:
    for i in range(len(arr)):
        for j in range(i+1):
            print(arr[i][j],end=" ")
        print()
        
if triangle==2:
    for i in range(len(arr)):
        for j in range(5-i):
            print(arr[i][j],end=" ")
        print()
