T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
 
    Max = arr[-1]
    price = 0
    for i in range(n - 1, -1, -1):
        if arr[i] > Max:
            Max = arr[i]
        else:
            price += Max - arr[i]
 
    print(f'#{test_case} {price}')