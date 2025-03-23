# def abc(lst):
#     global cnt
#     length = len(lst)
#     lst4 = []
#     if length > 1:
#         lst2 = abc(lst[:length//2])
#         lst3 = abc(lst[length//2:])
#
#         if lst2[-1] > lst3[-1]:
#             cnt += 1
#         idx2, idx3 = 0, 0
#         length2, length3 = len(lst2), len(lst3)
#         while True:
#             if idx2 >= length2:
#                 lst4 += lst3[idx3:]
#                 break
#             elif idx3 >= length3:
#                 lst4 += lst2[idx2:]
#                 break
#
#             if lst2[idx2] > lst3[idx3]:
#                 lst4.append(lst3[idx3])
#                 idx3 += 1
#             else:
#                 lst4.append(lst2[idx2])
#                 idx2 += 1
#
#         return lst4
#
#     return lst

def abc(lst):
    global cnt
    length = len(lst)
    if length > 1:
        lst2 = abc(lst[:length//2])
        lst3 = abc(lst[length//2:])

        if lst2[-1] > lst3[-1]:
            cnt += 1
        return sorted(lst2 + lst3)

    return lst

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = abc(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')
