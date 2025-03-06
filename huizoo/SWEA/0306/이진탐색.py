def abc(i):
    global last
    if i > n :
        return
    abc(2*i)
    arr[i] = last
    last += 1
    abc(2*i+1)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [0]*(n+1)
    last = 1
    abc(1)
    print(f'#{tc} {arr[1]} {arr[n//2]}')