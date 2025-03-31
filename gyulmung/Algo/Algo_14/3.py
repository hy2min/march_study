picA, picB = map(int, input().split())

count = 0
loop = 0

while loop < 1:
    if picA + (100 - picA) >= picB:
        count += 1
        picB += 1
        if picB == 100:
            break
    elif picB + (100 - picB) >= picA:
        count += 1
        picB += 1
        if picB == 100:
            break
print(count)