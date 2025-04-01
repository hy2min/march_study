import sys
sys.stdin = open('input.txt','r')

n = int(input())
arr = [input() for _ in range(n)]
lst = sorted(arr, key=lambda x:(len(x), x))
for i in range(n):
    print(lst[i])
