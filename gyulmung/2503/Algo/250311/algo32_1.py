import sys
sys.stdin=open('input.txt','r')

n = int(input())
lst = [input().split() for _ in range(n)]
ret = sorted(lst, key=lambda x : (x, x[1]))
for i in ret:
    print(*i)