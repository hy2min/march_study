arr = [4,1,2,3,5]

a = input()

if a == 'a' or a == 'b' or a == 'c':
    for i in arr[3::-1]:
        print(i,end=' ')
else:
    for i in arr[4:0:-1]:
        print(i,end=' ')


