t = int(input())
for tc in range(1, t+1) : 
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    max_multi = -21e8
    if n != m : 
        if n < m :    
            for i in range(m - n + 1) : 
                current_multi = 0
                for j in range(n) :
                    current_multi += arr1[j]*arr2[j+i]
                if max_multi < current_multi : 
                    max_multi = current_multi
        elif m < n :
            for i in range(n - m + 1) :
                current_multi = 0
                for j in range(m) : 
                    current_multi += arr1[j+i]*arr2[j]
                if max_multi < current_multi : 
                    max_multi = current_multi
    else :
        current_multi = 0 
        for i in range(n) : 
            current_multi += arr1[i]*arr2[i]
        if max_multi < current_multi : 
                max_multi = current_multi
    print(f'#{tc} {max_multi}')