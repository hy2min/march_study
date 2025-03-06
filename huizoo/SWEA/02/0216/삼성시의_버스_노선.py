t = int(input())
for tc in range(1, t+1):
    N = int(input())
    bus = [0]*5001
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            bus[i] += 1
    P = int(input())
    ans = []
    for _ in range(P):
        c = int(input())
        ans.append(bus[c])
    print(f'#{tc} {" ".join(map(str, ans))}')