map_arr = [
    [3, 55, 42],
    [-5, -9, -10]
]

pix = []
for _ in range(2):
    pix.append(list(map(int, input().split())))
arranged_map = [j for i in map_arr for j in i]
for i in pix:
    for j in i:
        if j in arranged_map:
            print("Y", end=" ")
        else:
            print("N", end=" ")
    print()