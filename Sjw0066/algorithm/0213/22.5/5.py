Map=[
    [3,5,4,2,2,3],
    [1,3,3,3,4,2],
    [5,4,4,2,3,5],
]
price=['T','P','G','K','C']

a,b=map(str,input().split())

col=ord(a)-ord('A')
row=int(b)-1

p_index = Map[col][row] - 1

print(price[p_index])