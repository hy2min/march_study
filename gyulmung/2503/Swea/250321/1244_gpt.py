
def rotation(lev, lst, rotate, Max):
    if lev == rotate:
        ret = int("".join(lst))
        Max = max(Max, ret)
        return Max

    for i in range(len(lst)):
        # 현재 숫자를 i번 위치에서 회전 시킨다
        lst[i] = lst[i]
        Max = rotation(lev + 1, lst, rotate, Max)
    return Max


T = int(input())
for test in range(1, T + 1):
    input_num = input().split()
    number, rotate = input_num
    number = list(number)
    rotate = int(rotate)

    # 회전 결과 저장하기
    Max = -1e8

    # 회전
    Max = rotation(0, number, rotate, Max)

    print(Max)
