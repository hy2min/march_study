string = list(map(str, input()))
Find_string = ['G','H','O','S','T']
count = 0
for i in range(len(string)):
    if string[i] == Find_string[0]:
        for j in range(len(Find_string)):
            if string[i + j] == Find_string[j]:
                count += 1


if count == 5:
    print('존재')
else:
    print('존재하지 않음')