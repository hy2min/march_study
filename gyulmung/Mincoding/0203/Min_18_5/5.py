arr = ['A', 'T', 'K', 'P', 'T', 'C', 'A', 'B', 'C']
string = list(map(str, input().split()))
ch1, ch2 = 0, 0


for i in range(9):
    if string[0] == arr[i]:
        ch1 = i
        break

for i in range(8, -1 , -1):
    if string[1] == arr[i]:
        ch2 = i
        break

print(ch2 - ch1)