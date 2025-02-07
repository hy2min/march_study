string = list(str(input()))
index = int(input())

string.pop(index)
print(*string, sep = '')