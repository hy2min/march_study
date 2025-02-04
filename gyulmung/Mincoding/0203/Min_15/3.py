arr = list(map(int, input().split()))

Flag = True
for i in range(5):
    if arr[i] - arr[i + 1] >= 3 or arr[i] - arr[i + 1] <= -3:
        Flag = False
        print('재배치필요')
        break
if Flag:
    print('완벽한배치')