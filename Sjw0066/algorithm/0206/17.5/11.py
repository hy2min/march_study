data=[3,5,4,2]

bit=list(map(int,input().split()))

for i in range(len(data)):
    data[i] *= bit[i]
print(sum(data))

