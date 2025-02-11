string = input()
n = len(string)

for i in range(n):
    for j in range(i+1,0,-1):
        print(string[n-j],end='')
    print()