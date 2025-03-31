height, width = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(height)]

lst = [(arr[i][j],i,j) for i in range(height) for j in range(width)]

lst.sort(key=lambda x:(-x[0],x[1],x[2]))

for i in range(3):
    print(f'{lst[i][0]}({lst[i][1]},{lst[i][2]})')
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

