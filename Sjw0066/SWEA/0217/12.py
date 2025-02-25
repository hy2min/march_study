heroes=['B','I','A','H']
n=int(input())

result=[]
index=0
while heroes:
    index=(n%len(heroes)) -1 + index
    result.append(heroes.pop(index))

print(' '.join(result))

