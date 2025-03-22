arr = ['ABCD','ABCE','AGEH','EIEI','FEQE','ABAD']
a = input()
lst = list(enumerate(a))
cnt = 0

actual = []
for i in range(4):
    if lst[i][1] != '?':
        actual.append(lst[i])

for word in arr:
    flag = True

    for idx, char in actual:
        if word[idx] != char:
            flag = False
            break

    if flag:
        cnt += 1

print(cnt)