while True:
    string = input()
    if len(string) <=10:
        break
max_s = 0
min_s = 91
for i in list(string):
    if max_s < ord(i):
        max_s = ord(i)
for i in list(string):
    if min_s > ord(i):
        min_s = ord(i)


max_idx = string.index(chr(max_s))
min_idx = string.index(chr(min_s))

print(max_idx)
print(min_idx)