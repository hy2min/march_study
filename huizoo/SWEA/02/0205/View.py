for tc in range(10):
    N = int(input())
    height = list(map(int, input().split()))
    total = 0
    for i in range(2, N-2):
        if height[i] == max(height[i-2:i+3]) : 
            current_max = 255
            for j in range(i-2, i+3) : 
                if j != i and current_max > height[i]-height[j]: 
                    current_max = height[i]-height[j]
            total += current_max

    print(f'#{tc+1} {total}')
