str = 'ATKPTCABC'
a, b = input().split()

for i in range(len(str)):
    if a == str[i]:
        idx1 = i
        break
for j in range(len(str)-1, -1, -1):
    if b == str[j]:
        idx2 = j
        break

ans = abs(idx1-idx2)
print(ans)
