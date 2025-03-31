ai = list(map(int, input()))
print(ai[0])

lst_numbers = [0]*10
for i in range(10):
    count = 0
    for j in range(len(ai) - 1):
        if i == ai[j]:
            count += 1
    lst_numbers[i] = count
print(lst_numbers)