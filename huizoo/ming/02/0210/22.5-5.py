a, b = input().split()

MAP = [
    [3,5,4,2,2,4],
    [1,3,3,3,4,2],
    [5,4,4,2,3,5],
]

price = ['T', 'P', 'G', 'K', 'C']

a_index = ord(a) - ord('A')
b_index = ord(b) - ord('1')

ans = price[MAP[a_index][b_index] - 1]

print(ans)