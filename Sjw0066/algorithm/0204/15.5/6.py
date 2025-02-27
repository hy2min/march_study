arr=[0]*9

for i in range(3):
    start_index,end_index=map(int,input().split())
    

    for j in range(start_index,end_index+1):
        arr[j] += 1

print(*arr)