from collections import deque

string = [input() for _ in range(4)]

p = deque()

while True:
    Min = 1e8
    Min_string = 'a'
    if len(p) == 4:
        break

    for i in range(len(string)):
        if len(string[i]) < Min:
            Min = len(string[i])
            Min_string = i
    p.append(string.pop(Min_string))
for i in range(4):
    print(f'{p[i]}')