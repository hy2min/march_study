arr = [
    [3,4,1,5],
    [3,4,1,3],
    [5,2,3,6],
]
a = int(input())
print(sum(list(zip(*arr))[a]))