arr = [
    [3,4,1,5],
    [3,4,1,3],
    [5,2,3,6],
]
arr2 = list(zip(*arr))
Sum = []
for row in arr2:
    Sum.append(sum(row))
n = int(input())
print(Sum[n])