import random

matrix = [[random.randint(0, 1) for _ in range(100)] for _ in range(100)]

for row in range(100):
    for j in range(100):
        print(matrix[row][j], end = " ")
    print()