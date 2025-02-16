t = int(input())
nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for tc in range(1, t+1):
    tcc, n = input().split()
    arr = list(input().split())
    arr.sort(key=lambda x: nums.index(x))
    ans = ' '.join(arr)
    print(f'#{tc} {ans}')