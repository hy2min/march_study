# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    L = int(input())
    arr = list(map(int,input().split()))
    ans = 0

    def merge_sort(Left, Right):

        global ans
        result = []
        Left_index = 0
        Right_index = 0
        L = len(Left)
        R = len(Right)

        while Left_index <= L - 1 and Right_index <= R - 1:
            if Left[Left_index] <= Right[Right_index]:
                result.append(Left[Left_index])
                Left_index += 1
            else:
                result.append(Right[Right_index])
                Right_index += 1

        if Right_index > R - 1:
            ans += 1
            while Left_index <= L - 1:
                result.append(Left[Left_index])
                Left_index += 1
            return result

        while Right_index <= R - 1:
            result.append(Right[Right_index])
            Right_index += 1
        return result


    def divide(lst):

        if len(lst) == 1:
            return lst

        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        last_left = divide(left)
        last_right = divide(right)

        return merge_sort(last_left, last_right)

    ans_result = divide(arr)
    print(f"#{tc} {ans_result[L//2]} {ans}")