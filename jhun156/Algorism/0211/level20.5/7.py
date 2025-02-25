string = input()
n = len(string)

for i in range(n):
    for j in range(i+1):
        print(string[j],end='')
    print()