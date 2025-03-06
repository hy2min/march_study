t = int(input())
for tc in range(1, t+1):
    n = int(input())
    st1 = list(map(int, input().split()))
    st2 = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if st1[i] != st2[i]:
            cnt+=1
            for k in range(i, n):
                st1[k] = (st1[k]+1)%2
    print(f'#{tc} {cnt}')