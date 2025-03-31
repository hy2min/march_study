pib = [0, 1] + [0] * 33
n = int(input()) -1
for i in range(2, 35):
    pib[i] = pib[i-1] + pib[i-2]
print(pib[n])
