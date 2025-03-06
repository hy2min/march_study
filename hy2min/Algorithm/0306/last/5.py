height, width = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(height)]
# lst = []
# for i in arr:
#     lst.extend(i)
# lst.sort(reverse=True)

# flag = 0
# for n in range(3):
#     for i in range(height):
#         for j in range(width):
#             if lst[n] == arr[i][j]:
#                 flag = 1
#                 print(f'{lst[n]}({i},{j})')
#                 break

lst = [(arr[i][j],i,j) for i in range(height) for j in range(width)]

lst.sort(key=lambda)