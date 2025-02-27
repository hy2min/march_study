string = list(input())
A, B = map(str, input().split())
w_AB = [0, 0]


for i in range(len(string)):
    if string[i] == A:
        w_AB[0] = i
    elif string [i] == B:
        w_AB[1] = i

for i in range(2):
    if w_AB[i]+1 >= len(string):
        continue
    string[w_AB[i]+1] = '#'
for j in range(2):
    if w_AB[j]-1 < 0:
        continue
    string[w_AB[j]-1] = '#'
string = ''.join(string)
print(string)