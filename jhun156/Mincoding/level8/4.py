arr = [i for i in map(int,input().split())]

for i in arr[::-1]:
    print(i,end = ' ')
    if i == 7:
        break
