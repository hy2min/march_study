train = [3, 7, 6, 4, 2, 9, 1, 7]
a,b,c=map(int,input().split())

for i in range(len(train)-2):
    if train[i] != a :
        continue
    for j in range(3):

