Map = [
    [3,5,4,2,2,3],
    [1,3,3,3,4,2],
    [5,4,4,2,3,5],
]
price = ['T','P','G','K','C']

a,b = input().split()
A = ord(a) - 65
B = int(b) - 1

k = Map[A][B] - 1
print(price[k])