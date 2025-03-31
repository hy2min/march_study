import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    TEST, N = map(str, input().split())
    arr = list(map(str, input().split()))
    num = int(N)
    dic ={"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    bucket = [0] * 10
    i = 0
    ret = []
    for name in dic:
        bucket[i] = arr.count(name)
        i += 1
    print(bucket)
    i = 0
    for name in dic:
        ret += [name] * bucket[i]
        i += 1
    print(f'#{test}')
    print(*ret)