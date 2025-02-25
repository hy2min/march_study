count = 0
arr = [i for i in map(int,input().split())]
lst = []
for i in range(2):
    row = []
    for j in range(3):
        row.append(arr[count])
        count += 1
    lst.append(row)

def Max():
    
    global lst
    temp = 0
    x,y = 0,0
    for i in range(2):
        for j in range(3):
            if lst[i][j] > temp:
                temp = lst[i][j]
                x,y = i,j
    return x,y

def Min():
    
    global lst
    temp = 100
    x,y = 0,0
    for i in range(2):
        for j in range(3):
            if lst[i][j] < temp:
                temp = lst[i][j]
                x,y = i,j
    return x,y

a,b = Max()
c,d = Min()
print(f"({a},{b})")
print(f"({c},{d})")