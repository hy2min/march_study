t = int(input())
for tc in range(1, t+1):
    st1, st2 = input().split()
    cnt = 0
    len1 = len(st1)
    len2 = len(st2)
    n = st1.count(st2)
    print(f'#{tc} {len1+(1-len2)*n}')