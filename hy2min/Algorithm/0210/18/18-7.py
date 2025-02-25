arr = [
    ['A','B','C'],
    ['A','G','H'],
    ['H','I','J'],
    ['K','A','B'],
    ['A','B','C'],
]
alp_count = [0] * 26
for alps in arr:
    for alp in alps:
        alp_count[ord(alp)-65] += 1
for i in range(25):
    if alp_count[i] > 0:
        print(chr(i+65) * alp_count[i] ,end="")