def Sum_numbers(ai):
    lst_numbers = [0]*10
    Max_num = 0 # 최대값
    counter = 0 # 최대값일때 좌표
    for i in range(10):
        count = 0
        for j in ai:
            if i == j:
                count += 1
        lst_numbers[i] = count
    for i in range(10):
        if Max_num <= lst_numbers[i]:
            Max_num = lst_numbers[i]
            counter = i
    return Max_num, counter

test_case = int(input())

for i in range(1, test_case + 1):
    N = int(input())
    ai = list(map(int, input()))
    Max_num, count = Sum_numbers(ai)
    print(f'#{i} {count} {Max_num}')


# def Max_numbers(lst_numbers):
#     Max_num = 0 # 최대값
#     count = 0 # 최대값일때 좌표
#     for i in range(10):
#         if Max_num <= lst_numbers[i]:
#             Max_num = lst_numbers[i]
#             count = i
#     return Max_num, count