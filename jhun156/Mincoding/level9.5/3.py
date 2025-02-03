arr = [
    ['D','A','A'],
    ['B','C','D'],
    ['E','F','A'],
    ['A','A','D'],
    ['F','G','E'],
]

a = input()

for i in range(5):
    for j in range(3):
        if arr[i][j] == a:
            print(f"({i},{j})")