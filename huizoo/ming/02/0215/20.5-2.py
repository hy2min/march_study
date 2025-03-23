st = input()
for i in range(len(st)):
    for j in range(i+1, 0, -1):
        print(st[-j], end ='')
    print()