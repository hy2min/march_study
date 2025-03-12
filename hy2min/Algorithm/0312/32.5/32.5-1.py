arr = ['ABCD', 'ABCE', 'AGEH', 'EIEI', 'FEQE', 'ABAD']
alp = [chr(i) for i in range(65, 91)]

s = input()
stack = []

for i in range(4):
    if s[i] in alp:
        stack.append([i,s[i]])
check = [0] * 6

for i in range(6):
    for idx, char in stack:
        if arr[i][idx] == char:
            check[i] = 1
        else:
            check[i] = 0

print(check.count(1))