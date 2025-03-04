T= 10

for tc in range(1, T + 1):
    tc = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    def row_max(arr1):
        max_sum = -21e8
        for i in arr1:
            sum1 = 0
            for j in i:
                sum1 += j
            if sum1 > max_sum:
                max_sum = sum1
        return max_sum


    def col_max(arr1):
        max_sum = -21e8
        for i in range(len(arr1)):
            sum1 = 0
            for j in range(len(arr1[i])):
                sum1 += arr1[j][i]
            if sum1 > max_sum:
                max_sum = sum1
        return max_sum


    def cross_max(arr1):
        max_sum = -21e8
        sum1 = 0
        for i in range(len(arr1)):
            sum1 += arr1[i][i]
            if sum1 > max_sum:
                max_sum = sum1
        sum1 = 0
        for i in range(len(arr1)):
            sum1 += arr1[i][-1 - i]
            if sum1 > max_sum:
                max_sum = sum1

        return max_sum

    check_max = []
    check_max.append(col_max(arr))
    check_max.append(row_max(arr))
    check_max.append(cross_max(arr))

    answer = 0
    for i in check_max:
        if i > answer:
            answer = i

    print(f'#{tc} {answer}')
