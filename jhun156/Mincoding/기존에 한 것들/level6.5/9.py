arr = [5,4,1,2,7,8]

a = int(input())

for i in range(a):
    for i in arr[::-1]:
        print(i,end = ' ')
    print()

