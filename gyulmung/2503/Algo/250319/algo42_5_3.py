import sys
sys.stdin = open('input.txt','r')

from collections import deque
import copy
def calculate(lev, Sum, trace):
    global count, lst
    if lev == n-1:
        if Sum == ans:
            count += 1
        return

    trace = copy.deepcopy(lst)
    a = lst.popleft()
    b = lst.popleft()

    arr = [(a+b)**2, max(a, b), (a-b)*(a+b), a**2 - b**2, ]
    for i in range(4):
        Sum = arr[i]
        lst.appendleft(Sum)
        calculate(lev+1, Sum, trace)
        lst.popleft()
    lst = trace



n = int(input())
nums = list(map(int, input().split()))

lst = deque()
for i in range(len(nums)):
    lst.append(nums[i])
# print(lst)

copy_lst = []
ans = 100
count = 0
calculate(0, 0, copy_lst)

print(count)
