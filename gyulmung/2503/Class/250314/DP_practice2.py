arr=[0,0,1,1]
lst = arr[::-1]
print(lst)
Sum = 0
for i in range(len(lst)):
    Sum += lst[i]*(2**i)
print(Sum)