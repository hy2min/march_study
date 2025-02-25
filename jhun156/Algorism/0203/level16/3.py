string = list(input())
num = int(input())

string.insert(num,'A')
for i in string:
    print(i,end='')