arr = [3, 2, 1, 3, 2, '테러범', 1]
arr2 = ['>>', '>>', '<<', '>>', '<<', '테러범', '<<']
n = int(input())
path = [n]
# while arr[n] != '테러범':
#     if arr2[n] == '>>':
#         n += arr[n]
#         path.append(n)
#     elif arr2[n] == '<<':
#         n -= arr[n]
#         path.append(n)
# for p in path[::-1]:
#     print(f'{p}번')

def dfs(x):
    if arr[x] == '테러범':
        for p in path[::-1]:
            print(f'{p}번')
        return
    if arr2[x] == '>>':
        x += arr[x]
    elif arr2[x] == '<<':
        x -= arr[x]
    if 0<x<7 and x not in path:
        path.append(x)
        dfs(x)
        path.pop()

dfs(n)