N = int(input())
arr = list(map(int,input().split()))
Min = sum(arr[0:4])
st = 0

cnt = 0
while cnt < N - 4:
    st += 1
    Min = min(Min,sum(arr[st:st+4]))
    cnt += 1

print(Min)