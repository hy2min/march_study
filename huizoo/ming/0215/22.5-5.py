a, b = input().split()
a = ord(a)-65
b = int(b)-1
MAP = [
    [3,5,4,2,2,3],
    [1,3,3,3,4,2],
    [5,4,4,2,3,5],
]
price = ['T','P','G','K','C']
print(price[MAP[a][b]-1])