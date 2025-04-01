import sys
sys.stdin = open('input.txt','r')

from collections import Counter
n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]
bits = [list(map(int, input().split())) for _ in range(n)]
lst = []
for i in range(n):
    for j in range(n):
        if bits[i][j] == 1:
            lst.append(numbers[i][j])
count = Counter(lst)
Max = sorted(lst, key=lambda x: (-count[x], x))
print(*Max)