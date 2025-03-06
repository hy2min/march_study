P = int(input())
for _ in range(P):
    arr = list(map(int, input().split()))
    tc = arr[0]
    arr = arr[1:]
    arr2 = [arr[0]]
    cnt = 0
    for i in range(1,20):
        arr2.append(arr[i])
        if arr2[-1] == max(arr2):
            pass
        else:
            for j in range(i):
                if arr2[j] > arr2[-1]:
                    cnt += len(arr2)-j-1
                    arr2.insert(j, arr2.pop())
                    break
    print(f'{tc} {cnt}')