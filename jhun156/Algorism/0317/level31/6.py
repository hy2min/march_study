arr = [1,2,3,3,5,1,0,1,3]
N = int(input())
Min = sum(arr[:N])

cnt = 0
while cnt < 9 - N + 1:
    Min = min(Min,sum(arr[cnt:cnt+N]))
    cnt += 1

print(Min)