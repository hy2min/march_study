t = int(input())
for tc in range(1, t+1):
    N = int(input())
    st = input()
    Max = 0
    for i in range(N):
        if st[i] == '1':
            cnt = 1
            for j in range(i+1, N):
                if st[j] != '1':
                    break
                elif st[j] == '1':
                    cnt += 1
            if Max < cnt:
                Max = cnt
    print(f'#{tc} {Max}')