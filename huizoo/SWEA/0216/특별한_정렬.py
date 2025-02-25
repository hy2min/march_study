t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr2 = []
    for i in range(10):
        if i % 2 == 0:
            arr2.append(arr[N-(i+2)//2])
        elif i % 2 == 1:
            arr2.append(arr[(i+1)//2-1])
    print(f'#{tc} {" ".join(map(str, arr2))}')