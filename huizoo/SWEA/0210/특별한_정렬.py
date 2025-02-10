T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    numbers2 = []
    for i in range(10) :
        if i % 2 == 0 :
            numbers2.append(numbers[-(i+2)//2])
        else :
            numbers2.append(numbers[(i-1)//2])
    ans = ' ' .join(map(str, numbers2))
    print(f'#{tc} {ans}')