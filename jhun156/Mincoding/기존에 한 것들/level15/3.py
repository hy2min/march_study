arr = [i for i in map(int,input().split())]

for i in range(len(arr)-1):
    if abs(arr[i]-arr[i+1]) >= 3:
        print("재배치필요")
        break
else:
    print("완벽한배치")