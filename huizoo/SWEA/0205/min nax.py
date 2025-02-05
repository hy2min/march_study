T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_numbers = numbers[0]
    min_numbers = numbers[0]
     
    for i in range(N) : 
        if max_numbers < numbers[i] : 
            max_numbers = numbers[i]
        elif min_numbers > numbers[i] : 
            min_numbers = numbers[i]
 
    print(f'#{tc+1} {max_numbers-min_numbers}')


# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     print(f'#{test_case} {max(numbers)-min(numbers)}')