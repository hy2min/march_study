import sys
sys.stdin = open('input.txt','r')

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
Sum = 0
for i in range(N):
    Sum += arr[i]*(N-i)
print(Sum)