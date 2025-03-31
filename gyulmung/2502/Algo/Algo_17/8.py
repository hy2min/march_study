vect = ['B', 'T', 'K', 'I', 'G', 'Z']
target = list(map(str, input().split()))

count = 0
for i in range(len(target)):
    for j in range(len(vect)):
        if vect[j] == target[i]:
            count += 1

print(count)