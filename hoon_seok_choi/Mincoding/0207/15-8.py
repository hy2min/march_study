a = input()
b = input()
c = input()
d = input()
e = input()

arr = [a,b,c,d,e]

max_s = arr[0]


for i in range(5) :
    if len(max_s) < len(arr[i]) :
        max_s = arr[i]


print(max_s)