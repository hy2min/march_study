import sys
sys.stdin = open('input.txt', 'r')


from collections import deque
def in_order(now):
    if now > len(lst) - 1:
        return

    in_order(now*2)
    in_order(now*2+1)
    number.append(lst[now])
T = 10
for test in range(1, T+1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(input().split()))
    # print(arr)
    lst = [0]
    for i in arr:
        lst.append(i[1])
    # print(lst)
    number = deque()
    ret = []
    hide = []
    in_order(1)
    # print(number)

    for i in number:
        if i.isdigit():
            ret.append(int(i))
        else:
            a = ret.pop()
            b = ret.pop()
            if i == '+':
                ret.append(b+a)
            elif i == '-':
                ret.append(b-a)
            elif i == '*':
                ret.append(b*a)
            elif i == '/':
                ret.append(b//a)
    print(f'#{test}', *ret)

# if not number:
#     a = ret.pop()
#     b = ret.pop()
#     c = hide.pop()
#     if c == '+':
#         ret.append(a + b)
#     elif c == '-':
#         ret.append(a - b)
#     elif c == '*':
#         ret.append(a * b)
#     elif c == '/':
#         ret.append(a // b)
# if i.isdigit():
#     ret.append(int(i))
# else:
#     if len(ret) < 2:
#         hide.append(i)
#     else:
#         a = ret.pop()
#         b = ret.pop()
#         if i == '+':
#             ret.append(a + b)
#         elif i == '-':
#             ret.append(a - b)
#         elif i == '*':
#             ret.append(a * b)
#         elif i == '/':
#             ret.append(a // b)
