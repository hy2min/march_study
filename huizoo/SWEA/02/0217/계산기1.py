# def dfs(lst):
#     stack = []
#     for num in lst:
#         if num == '+':
#             b = stack.pop()
#             a = stack.pop()
#             stack.append(a + b)
#         else:
#             stack.append(int(num))
#     return stack[0]
#
# for tc in range(1, 11):
#     N = int(input())
#     arr = list(input())
#     for i in range(1, N, 2):
#         arr[i], arr[i+1] = arr[i+1] + arr[i]
#     ret = dfs(arr)
#     print(f'#{tc} {ret}')
#
#
#
#
N = 10

arr = [input() for _ in range(N)]
print(arr)
