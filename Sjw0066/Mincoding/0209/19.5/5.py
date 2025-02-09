image=[list(input()) for _ in range(3)]

dat=[0]*100
for i in image:
    for j in i:
        dat[ord(j)] += 1 

for i in range(len(dat)):
    if dat[i]:
        print(chr(i),end="")