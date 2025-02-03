a,b = map(int,input().split())

sum = 0

if a >= b:
    sum = a - b
else:
    sum = b - a

if sum % 2 == 1:
    print("고백한다")
else:
    print("짝사랑만")