import sys
sys.stdin = open('input.txt','r')

n = int(input())
arr = [1, 2, 3, 3, 5, 1, 0, 1, 3]
Sum = 0
for i in range(n):
    Sum += arr[i]
Min = Sum

for i in range(9-n):
    Sum += arr[i+n]
    Sum -= arr[i]
    if Min > Sum:
        Min = Sum

print(Min)