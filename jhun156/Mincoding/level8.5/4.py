arr = [0] * 17

def Input():
    a,b,c = input().split()
    return a,b,c

A,B,C = Input()

for i in range(7):
    arr[i] = A
for i in range(7,13):
    arr[i] = B
for i in range(13,17):
    arr[i] = C

arr.reverse()

for i in arr:
    print(i,end='')