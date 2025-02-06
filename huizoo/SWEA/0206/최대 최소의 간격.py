t = int(input())
for tc in range(1, t+1) : 
    n = int(input())
    arr = list(map(int, input().split()))
    min_index = arr.index(min(arr))
    max_index = n-1-arr[::-1].index(max(arr))
    print(f'#{tc} {abs(min_index-max_index)}')
    