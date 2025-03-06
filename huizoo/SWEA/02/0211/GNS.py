t = int(input())
for _ in range(t):
    tc, N = input().split()
    numbers = list(input().split())
    dic = {
        'ZRO': 0,
        'ONE': 1,
        'TWO': 2,
        'THR': 3,
        'FOR': 4,
        'FIV': 5,
        'SIX': 6,
        'SVN': 7,
        'EGT': 8,
        'NIN': 9,
    }
    numbers.sort(key=lambda x: dic[x])
    # numbers.sort(key=dic.get)

    print(f'{tc}', end=" ")
    print(*numbers)