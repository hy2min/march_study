# problem 6
#
# lst=[[4, 2, 3, 5],
#      [1, 1, 2, 3],
#      [4, 7, 6, 4]]
#
# target=[[1, 2],
#         [7, 6]]
#
# def find_num(x):
#     count = 0
#     for i in lst:
#         for j in i:
#             if j == x:
#                 count += 1
#     return count
#
# for i in target:
#     for j in i:
#         print(f'{j}:{find_num(j)}')

#
#
# def sum(y,x):
#     z=y+x
#     z+=1
#     return z
# a=10
# b=20
# b=30
# b=40
# b=50
# b=60
#
# ret=sum(a,b)
# print(ret)
#
# for i in range(300):
#     if i == 1:
#         debug=1
#     for j in range(6000):
#         print('#')
# import sys
# sys.stdin=open('input.txt','r')
#
# arr = list(map(int, input().split()))
# for i in range(0, 5):
#     for j in range(i + 1, 6):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print(*arr)
#

# import sys
# sys.stdin=open('input.txt','r')
# arr = list(map(int, input().split()))
# lst = []
# for i in range(6):
#     lst.append(arr[i])
#     for j in range(i, 0, -1):
#         if lst[j] < lst[j-1]:
#             lst[j-1],lst[j] = lst[j],lst[j-1]
#         else:
#             break
# print(*arr)

import sys
sys.stdin=open('input.txt','r')
arr = list(map(int, input().split()))

for i in range(6, 0, -1):
    for j in range(5):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)