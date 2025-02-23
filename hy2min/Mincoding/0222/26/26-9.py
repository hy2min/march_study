string = input()
data = list(map(int, input().split()))
for i in range(len(data)):
    print(string[data[i]], end="")