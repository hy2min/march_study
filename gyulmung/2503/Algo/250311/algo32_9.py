import sys
sys.stdin = open('input.txt','r')
from collections import Counter

arr = list(input())
n = int(input())

arr.sort()

lst = []
for i in range(n):
    lst.append(arr.pop())
count = Counter(lst)
print(max(count, key=lambda x:count[x]))