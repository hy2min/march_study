# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    test_case,n = input().split()
    N = int(n)
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    arr = list(input().split())
    target = []
    for i in range(10):
        tmp = arr.count(numbers[i])
        target.append(tmp)
    ans = []
    for i in range(10):
        ans.extend([numbers[i]] * target[i])

    print(test_case)
    print(*ans)