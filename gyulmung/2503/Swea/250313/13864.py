import sys
sys.stdin = open('input.txt','r')
T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    group = []

    group.append(arr[0:])
    print(f'{test} {ans}')