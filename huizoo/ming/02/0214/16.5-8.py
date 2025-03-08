arr = [
    ['A',7,9,'T','K','Q'],
    ['M','I','N','C','O','D'],
]
a, b = input().split()
if a in arr[0]+arr[1]:
    print(f'{a} : 존재')
else :
    print(f'{a} : 없음')
if b in arr[0]+arr[1]:
    print(f'{b} : 존재')
else :
    print(f'{b} : 없음')