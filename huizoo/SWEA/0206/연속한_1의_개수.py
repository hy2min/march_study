T = int(input())
for tc in range(1, T+1) : 
    N = int(input())
    arr = input()
    one_arr = arr.split('0')
    print(f'#{tc} {len(max(one_arr))}')
