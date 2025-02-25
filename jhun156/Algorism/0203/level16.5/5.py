string = list(input())
a = input()
b = input()

for i in range(len(string)):
    if string[i] == a:
        string[i] = b
none_string = ''
for i in string:
    none_string += i
print(none_string)