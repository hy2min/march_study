import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    A, B = map(str, input().split())
    cnt = 0
    ret = 0
    for i in range(len(A)):
        slice_x = i + len(B)
        if A[i:slice_x] == B:
            cnt += 1
    ret = len(A) - (len(B)-1) * cnt
    print(f'#{test} {ret}')
