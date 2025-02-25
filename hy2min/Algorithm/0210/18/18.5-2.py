arr = list(map(int, input().split()))
flag = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            flag = 1
            print("도플갱어 발견")
            break
    if flag == 1:
        break
if flag == 0:
    print("미발견")
