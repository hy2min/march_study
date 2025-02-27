vect=[3,5,1,1,2,3,2]

arr=list(map(int,input().split()))

for i in arr:
    print(f'{i}={vect.count(i)}개')