arr = [3,5,1,9,7]
for i in range(4) : 
    if input() == 'R' : 
        temp = arr[-1]
        arr = arr[:-1]
        arr.insert(0, temp)
    else : 
        temp = arr[0]
        arr = arr[1:]
        arr.append(temp)

print(*arr)